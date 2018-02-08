from tkinter import *
import random
import math
 
window = Tk()
 
window.title("Multiplying Exercises")
 
window.geometry('350x150')
 
lbl = Label(window, text="Enter Number Range")
 
lbl.grid(column=0, row=0)

spin = Spinbox(window, from_=2, to=9, width=5,textvariable=8)

spin.grid(column=1,row=0)

spin1 = Spinbox(window, from_=3, to=9, width=5)

spin1.grid(column=2,row=0)

txt = Entry(window,width=10,textvariable="papi chulo")
 
txt.grid(column=1, row=1)


lbl2 = Label(window, text="")
lbl2.grid(column=0, row=1)


lbl3 = Label(window, text=" ")
lbl3.grid(column=0, row=2)

firstNumber=2
SecondNumber=2
lbl2.configure(text="What is "+str(firstNumber)+" times "+str(SecondNumber)+"?")
final=firstNumber*SecondNumber

def PutNewNumbers():
	global firstNumber
	global SecondNumber
	global final
	enteredValue=int(txt.get())
	if enteredValue==final:
		lbl3.configure(text="Right answer!")
		firstNumber=random.randrange(int(spin.get()), int(spin1.get()))
		SecondNumber=random.randrange(int(spin.get()), int(spin1.get()))
		lbl2.configure(text="What is "+str(firstNumber)+" times "+str(SecondNumber)+"?")
		final=firstNumber*SecondNumber
	elif enteredValue!=final:
		lbl3.configure(text="Wrong answer. It should have been "+str(final))
		firstNumber=random.randrange(int(spin.get()), int(spin1.get()))
		SecondNumber=random.randrange(int(spin.get()), int(spin1.get()))
		lbl2.configure(text="What is "+str(firstNumber)+" times "+str(SecondNumber)+"?")
		final=firstNumber*SecondNumber
	    





btn = Button(window, text="Answer", command=PutNewNumbers)

btn.grid(column=2, row=1)
 
window.mainloop()
