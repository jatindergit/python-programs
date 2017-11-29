from Tkinter import *

def iCalc(source,side):
	storeObj = Frame(source, botherwidth=4, bd=4, bg="powder blue")
	storeObj.pack(side=side,expand=YES,file=BOTH)
	return storeObj
	
def button(source,side, text,command=None):
	storeObj = Button(source, text=text,command=command)
	storeObj.pack(side=side,expand=YES,file=BOTH)
	return storeObj
	
class app(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.option_Add('*Font','arial 20 bold')
		self.pack(expand=YES,fill=BOTH)
		self.master.title('Calculator')

import tkinter

tkinter._test()
