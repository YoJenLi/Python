# -*- coding: utf-8 -*-
import requests
import os
import sys
import re
from bs4 import BeautifulSoup as bs
from time import time
from time import strftime
requests.packages.urllib3.disable_warnings()

rs = requests.session()

def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c,'')
    return value.rstrip();

def store_art(CrawlerTime, url, rate="", title="" ):
    res=rs.get(url,verify=False)
    soup=bs(res.text,'html.parser')

    
    board = url.strip('https://www.ptt.cc/bbs/').split('/index.html')[0]
    # relative_path = os.path.join(CrawlerTime,board)建立路徑 join
    path = os.path.abspath(CrawlerTime)#絕對路徑

    try:
    	if not os.path.exists(path):
    		os.makedirs(path) 
    except Exception, e:
    	print 'os.makedirs(path) error' 
    try:
        filename = remove(title, '\/:*?"<>|.') + ".txt" 
        title1 = remove(title, '\/:*?"<>|.').encode('utf-8')
        content = soup.select('#main-container')[0].text.split('--')[0].encode('utf-8')
        time = soup.select('.article-meta-value')[3].text.encode('utf-8')
        url = 'https://www.ptt.cc/bbs/'+ board.encode('utf-8')
              
        with open(CrawlerTime +"/"+ filename, 'w') as f: 
                 f.write(title1+','+time+','+url+','+content) 
    except IndexError:
        pass              


def main():
    print "Crawler Parsing...."

    name1 = crawlName(url)
    CrawlerTime= name1+'-'+strftime("%Y-%m-%d[%H-%M-%S]")


    ts = time()
    article_urls = []
    total=0
    for article_url in article_urls:
        count+=1
        print "Crawling: " + str(100 * count / total ) + " %."
        store_art(CrawlerTime,board)
        
    print('Time {}s'.format(time() - ts))
    print "Crawler End...."

if __name__ == '__main__':
    main()