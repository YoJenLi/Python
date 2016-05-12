# -*- coding: utf-8 -*-
import requests
import sys
import download_article
from bs4 import BeautifulSoup as bs
from time import time
from time import strftime
requests.packages.urllib3.disable_warnings()

rs=requests.session()
# 從網址中找到index和.html字串，startIndex+5是要取index這五個字元往後到.html中間的值
# https://www.ptt.cc/bbs/Tech_Job/index2204.html
def getPageNumber(content):
    startIndex = content.find('index')
    endIndex = content.find('.html')
    pageNumber = content[startIndex+5 : endIndex]
    return pageNumber
# 需要的參數有 
def crawPage(url, article_list, push_rate):
    res = rs.get(url,verify=False)
    soup = bs(res.text,'html.parser')

    for r_ent in soup.select('div.r-ent'):  #從<div class="r-ent">找尋需要的元素
        try:
            atag=r_ent.select('div.title')[0].find('a') 
            #<div class="title"><a href="/bbs/Tech_Job/M.1463024248.A.2AE.html">atag</a> 標題名稱
            if(atag):
                #找到文章連結
                URL = atag['href'] 
                #文章標題
                title = r_ent.select('div.title')[0].text.strip()
                #文章連結 https://www.ptt.cc/bbs/Tech_Job/M.1463024248.A.2AE.html
                URL = 'https://www.ptt.cc' + URL 
                #推文數在<div class="nrec"></div>
                rate = r_ent.select('div.nrec')[0].text

                if(rate):
                    comment_rate = rate
                    if rate == u'爆':
                        comment_rate = 100
                    if rate[0] == 'X':
                        comment_rate = -1 * int(rate[1])
                else:
                    comment_rate = 0

                if int(comment_rate) >= push_rate:
                    article_list.append((int(comment_rate), URL, title))
        except:
            print 'error:',URL
def crawlName(url):
	front = url.find('/bbs/')
	end = url.find('/index.html')
	crawlName = url[fornt+5:end]
	return crawlName

if __name__ == '__main__':
    #從cmd輸入 開始的頁數,想爬取的總頁數,推文數,欲爬取版的網址
    start_page, page_term, push_rate, url = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
    ts = time()
    name = crawlName(url)
    CrawlerTime = name + strftime("%Y-%m-%d[%H-%M-%S]")
    if start_page < 0:
        res = rs.get(url,verify=False)
        soup = bs(res.text,'html.parser')
        #<a class = "btn wide" href = "/bbs/Tech_Job/index2204.html">上頁</a> 有兩個btn wide 抓取第二個
        ALLpageURL = soup.select('.btn.wide')[1]['href']
        #start_page 會輸入-1 所以總頁數會+1=2204
        ALLpage = start_page = int(getPageNumber(ALLpageURL))+1

    print "Analytical download page...."

    article_list = []
    #range(-1,-1-2204,-1): 2204 2203 2202 2201.......
    for page in range(start_page, start_page - page_term, -1):
    	#https://www.ptt.cc/bbs/Tech_Job/index2204.html 
        page_url = url.strip().split('.html')[0] + str(page) + '.html'
        crawPage(page_url,article_list,push_rate)

    total = len(article_list)
    count = 0
    for hot_rate, url ,title in article_list:
        download1.store_art(CrawlerTime, url ,str(hot_rate),title)
        count += 1
        print "Download: " + str(100 * count/ total) + " %."

    print "DONE"
    print('Time {}s'.format(time() - ts))