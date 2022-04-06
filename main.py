from tkinter import *

testWindow = Tk()
testWindow.title("Testing... 1 2...")

testString = StringVar()
testString.set("Hello World!")
testLabel = Label(testWindow, textvariable = testString, padx = 20, pady = 20)
testLabel.grid(column=1,row=1)

def doneChecking():
    testWindow.destroy()

string = StringVar()
string.set("Looks good")
testButton = Button(testWindow, textvariable = string, padx = 20, pady = 20,font="Calibri", command = lambda: doneChecking())
testButton.grid(column=1,row=2)

testWindow.mainloop()