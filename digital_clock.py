import sys
from tkinter import *
from time import *


def tick():
    t=strftime("%H:%M:%S")
    clock.config(text=t)
    clock.after(160,tick)

window=Tk()
window.title("DIGITAL CLOCK")
clock=Label(window,font=("times",200,"bold"),bg="yellow",fg="black")
clock.grid(row=0,column=1)
tick()


mainloop()
