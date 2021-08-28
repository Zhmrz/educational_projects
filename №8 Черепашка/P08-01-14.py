#Пять квадратов
from turtle import *
shape("turtle")

for p in range(4):
    penup()
    setheading(p*90)
    forward(120)
    pendown()
    setheading(0)
    for i in range(4):
        left(90)
        forward(90)
penup()
goto(60,60)
pendown()
for i in range(4):
    left(90)
    forward(90)

hideturtle()
