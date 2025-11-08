from turtle import *

# To draw random patterns, by using circle in "for" loop
bgcolor("black")
speed(0)
hideturtle()

for i in range(220):
    color("red")
    circle(i)
    color("orange")
    circle(i*0.8)
    right(3)
    forward(3)

done()