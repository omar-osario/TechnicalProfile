import Tkinter
from gen import *

class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
	
	def initialize(self): 
		self.grid()
		
		self.entryVariable = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
		self.entry.grid(column=0, row=0, sticky='EW') 
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set('Enter Text Here Wiseman')

		button = Tkinter.Button(self,text="Click me !", command=self.OnButtonClick)
		button.grid(column=1,row=0)
		
		self.applicationText = Tkinter.StringVar()
		self.applicationText.set('Enter Applicaiton Here')
		
		self.labelVariable = Tkinter.StringVar()
		label = Tkinter.Label(self,textvariable=self.labelVariable, anchor="w", fg="white", bg="blue") 
		label.grid(column=0, row=1, columnspan=2, sticky='EW')
		self.labelVariable.set('Hello Hello Hello !')
		
		self.labelVariable2 = Tkinter.StringVar()
		label2 = Tkinter.Label(self,textvariable=self.labelVariable2, anchor="w", fg="green", bg="black") 
		label2.grid(column=0, row=2, columnspan=2, rowspan=20, sticky='EW')
		self.labelVariable2.set('Logging')

		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(0,weight=1)
		self.resizable(True,True)
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)
		self.update()
		self.geometry(self.geometry()) 

	def OnButtonClick(self):
		print 'you clicked the button!!'
		self.labelVariable.set( self.entryVariable.get()+ 'you clicked the button!!')
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)
		
	def OnPressEnter(self,event):
		print 'you press the <return> key!'
		self.labelVariable.set( self.entryVariable.get()+ 'you press the <return> key!')
		self.labelVariable2.set( self.labelVariable2.get() + '\n' + self.entryVariable.get())
		
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)


if __name__ == "__main__" :
	app = simpleapp_tk(None)
	app.title('Prime Search')
	app.mainloop()
"""
"""