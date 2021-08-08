import turtle
wn=turtle.Screen()
wn.title("nikhil")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

score_a=0
score_b=0
pad_a=turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

pad_b=turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.up()
pen.goto(0,260)
pen.hideturtle()
pen.write("PLAYER A::0  PLAYER B::0",align="center",font=('Arial',24,'normal'))

def pad_a_up():
    y=pad_a.ycor()
    y=y+20
    pad_a.sety(y)

def pad_a_down():
    y=pad_a.ycor()
    y=y-20
    pad_a.sety(y)


def pad_b_up():
    y=pad_b.ycor()
    y=y+20
    pad_b.sety(y)

def pad_b_down():
    y=pad_b.ycor()
    y=y-20
    pad_b.sety(y)

wn.listen()
wn.onkeypress(pad_a_up,"w")
wn.onkeypress(pad_a_down,"s")
wn.onkeypress(pad_b_up,"Up")
wn.onkeypress(pad_b_down,"Down")


 

while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a=score_a+1
        pen.clear()
        pen.write("PLAYER A::{}  PLAYER B::{}".format(score_a,score_b),align="center",font=('Arial',24,'normal'))
    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b=score_b+1
        pen.clear()
        pen.write("PLAYER A::{}  PLAYER B::{}".format(score_a,score_b),align="center",font=('Arial',24,'normal'))

    if (ball.xcor()>340 and ball.xcor()<350)and(ball.ycor()<pad_b.ycor()+40 and ball.ycor()>pad_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1

    if (ball.xcor()<-340 and ball.xcor()>-350)and(ball.ycor()<pad_a.ycor()+40 and ball.ycor()>pad_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
