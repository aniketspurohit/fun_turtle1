from turtle import *
from random import randint
bgcolor('black')
speed(30)
x=1
while(x<350):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    colormode(255)
    pencolor(r,g,b)
    fd(45 + x)
    rt(90.991)

    x = x+1
exitonclick()