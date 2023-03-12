from tkinter import *

def run():
     runs = inputbox.get(1.0, END)
     exec(runs)

root = Tk()

runbtn = Button(text="Run", command=run).place(x=0,y=0)

inputbox = Text()

inputbox.place(x=0, y=20)

root.title('Python IDE')
root.geometry('400x500')
root.mainloop()