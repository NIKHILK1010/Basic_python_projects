import os
import turtle
import time
import random
wn=turtle.Screen()
wn.title("snake")
wn.bgcolor("green")
wn.setup(600,600)
wn.tracer(0)

score=0
high_score=0
#snakehead
head=turtle.Turtle()
head.shape("square")
head.speed(0)
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#food
food=turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("red")
food.penup()
food.goto(0,100)
segments=[]

#pen
pen=turtle.Turtle()
pen.shape("circle")
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score : 0  high_score : 0",align="center",font=("Arial",20,"normal"))

#function
def goup():
    if head.direction!="down":
        head.direction="up"

def godown():
    if head.direction!="up":
        head.direction="down"
    
def goleft():
    if head.direction!="right":
         head.direction="left"
   
def goright():
    if head.direction!="left":
        head.direction="right"
    

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x-20)


wn.listen()
wn.onkeypress(goup,"w")
wn.onkeypress(godown,"s")
wn.onkeypress(goleft,"d")
wn.onkeypress(goright,"a")

while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
         time.sleep(1)
         head.goto(0,0)
         head.direction="stop"

         for segment in segments:
             segment.goto(1000,1000)
         segments.clear()

    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score +=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("score : {} high_score : {}".format(score,high_score),align="center",font=("Arial",20,"normal"))
       

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
    time.sleep(0.1)

wn.mainloop()
