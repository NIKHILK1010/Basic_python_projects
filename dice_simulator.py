from random import *
from tkinter import *

window=Tk()
window.title("dice simulator")
window.geometry("500x400")

l1=Label(window,fg="blue",font=("bold",200,"normal"),text='')
l1.place(x=150,y=00)

def roll():
    d=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.configure(text=f'{choice(d)}')
    l1.pack()
    print("NEXT")

b1=Button(window,bg="black",fg="white",font=("bold",20,"normal"),text="roll dice",command=roll)
b1.place(x=200,y=290)



window.mainloop()
