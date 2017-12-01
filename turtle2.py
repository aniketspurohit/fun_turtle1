from turtle import *
from random import randint

bgcolor('black')
speed(45)
x = 1
colormode(255)
#pencolor(randint(0,255),randint(0,255),randint(0,255))
color('red','red')
begin_fill()
lt(50)
fd(150)
while(x<10):
    fd(26)
    lt(25)
    x=x+1
rt(165)
y = 1
while(y<10):
    fd(25)
    lt(25)
    y=y+1
rt(26)
fd(150)
end_fill()
done()



