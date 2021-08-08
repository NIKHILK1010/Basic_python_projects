from turtle import *
from random import *
from time import sleep

bgcolor("yellow")
t1=Turtle()
t1.shape("turtle")
t1.left(90)
t2=t1.clone()
t1.shapesize(4)
t2.shapesize(4)
t1.penup()
t2.penup()
t1.color("red")
t2.color("blue")
t1.goto(-150,-150)
t2.goto(150,-150)

t3=Turtle()
t3.penup()
t3.goto(-200,200)
t3.pendown()
t3.pensize(10)
t3.forward(450)
t3.pencolor("green")
t3.write("FINISH",align="right",font=("bold",20))

sleep(2)
for i in range(140):
    t1.forward(randint(1,3))
    t1.left(5)
    t1.right(5)
    t2.left(5)
    t2.right(5)
    t2.forward(randint(1,3))


mainloop()
