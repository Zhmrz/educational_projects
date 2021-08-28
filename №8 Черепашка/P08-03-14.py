#Спираль
from turtle import *
shape("turtle")

p=1
while p<18:
    forward(2*p)
    left(30-p)
    p+=0.4
hideturtle()
