#Поворачивающийся квадрат
from turtle import *
shape("turtle")
left(90)
i=100
q=20
while i>55:
    for k in range(3):
        forward(i-q)
        right(91)
        q+=0.3
    i-=1
hideturtle()
