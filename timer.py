from time import *
from turtle import *

hrs=0
minu=0
sec=0
t1=Turtle()
t1.color("red")
bgcolor("green")
setup(800,300)
penup()
goto(0,0)
while True:
    t1.write(str(hrs).zfill(2)+":"+str(minu).zfill(2)+":"+str(sec).zfill(2),font=("arial",50,"normal"))
    sec=sec+1
    sleep(1)

    if sec==60:
          sec=0
          minu=minu+1

  
    if minu==60:
         minu=0
         hrs=hrs+1

    t1.clear()



