from Tkinter import *
import ttk
from encrypt import Encrypt
import os


class EncryptGUI(Frame):
	def __init__(self,master = None):
		Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
		self.e = None
		self.userinput = ""
		self.result = ""


	
	def createWidgets(self):
		self.it = Label(self)
		self.it["text"] = "Input:"
		self.it.grid(row = 0, column = 0)
		self.ifd = Entry(self)
		self.ifd["width"] = 60
		self.ifd.grid(row = 0, column = 1, 
						columnspan = 6)

		self.ot = Label(self)
		self.ot["text"] = "Output:"
		self.ot.grid(row = 1,column = 0)
		self.ofd = Entry(self)
		self.ofd["width"] = 60
		self.ofd.grid(row = 1, column = 1,
						columnspan = 6)
		
		self.nb = Button(self)
		self.nb["text"] = "New"
		self.nb.grid(row = 2, column = 0)
		self.nb["command"] = self.nm
		
		self.lb = Button(self)
		self.lb["text"] = "Load"
		self.lb.grid(row = 2, column = 1)
		self.lb["command"] = self.lm
		
		self.sb = Button(self)
		self.sb["text"] = "Save"
		self.sb.grid(row = 2, column = 2)
		self.sb["command"] = self.sm
		
		self.eb = Button(self)
		self.eb["text"] = "Encode"
		self.eb.grid(row = 2, column = 3)
		self.eb["command"] = self.em
		
		self.db = Button(self)
		self.db["text"] = "Decode"
		self.db.grid(row = 2, column = 4)
		self.db["command"] = self.dm

		self.cb = Button(self)
		self.cb["text"] = "Clear"
		self.cb.grid(row = 2, column = 5)
		self.cb["command"] = self.cm

		self.cb2 = Button(self)
		self.cb2["text"] = "Copy"
		self.cb2.grid(row = 2, column = 6)
		self.cb2["command"] = self.cm2

		self.dt = Label(self)
		m = "something happend"
		self.dt["text"] = m
		self.dt.grid(row = 3, column = 0,
					columnspan = 7)

	def nm(self):
		self.e = Encrypt()
		self.dt["text"] = self.e	

	def lm(self):
		if os.path.exists("./code.txt"):
			f = open('./code.txt', 'r')
			code = f.readline()
			self.e = Encrypt(code)
			s = str("".join(self.e.code))
			m = "code: " + s
			self.dt["text"] = m
		else:
			m = "Load denied!!"
			self.dt["text"] = m	
	def sm(self):
		if self.e == None:
			m = "It can not save!!"
			self.dt["text"] = m
		else:
			f = open('./code.txt','w')
			f.write("".join(self.e.code))
			f.close()
			self.dt["text"] = "It's Done."	
	
	def em(self):
		self.userinput = self.ifd.get()
		if self.userinput == "":
			m = "No input string!!!"
			self.dt["text"] = m
		else:
			if self.e == None:
				m = "No encrypt object!!"
				self.dt["text"] = m
			else:
				s = self.userinput
				r = self.e.toEncode(s)
				self.result = r
				self.ofd.delete(0, 200)
				self.ofd.insert(0, r)
				m = "Encoding success!!"
				self.dt["text"] = m

	def dm(self):
		self.userinput = self.ifd.get()

		if self.userinput == "":
			m = "No input string!!"
			self.dt["text"] = m
		else:
			if self.e == None:
				m = "No encrypt object!!"
				self.dt["text"] = m
			else:
				s = self.userinput
				r = self.e.toDecode(s)
				self.result = r
				self.ofd.delete(0, 200)
				self.ofd.insert(0, r)
				m = "Decoding success!!"
				self.dt["text"] = m

	def cm(self):
		self.e = None
		self.userinput = ""
		self.result = ""
		self.ifd.delete(0, 200)
		self.ofd.delete(0,200)
		self.dt["text"] = "Clear all!!!"

	def cm2(self):
		if self.result == "":
			m = "Copy denied!!"
			self.dt["text"] = m
		else:
			self.cliphorad_clear()
			r = self.result
			self.cliphorad_clear(r)
			m = "It is copied."	
			self.dt["text"] = m				




if __name__ == '__main__':
	root = Tk()
	app = EncryptGUI(master = root)
	app.mainloop()











