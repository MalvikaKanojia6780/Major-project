import turtle
from random import randint
t=turtle.Turtle()
turtle.bgcolor("black")

# Draw Moon
t.penup()
t.goto(-300,150)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(70)
t.end_fill()
t.penup()
t.goto(-270,150)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(70)
t.end_fill()

# Write Eid Mubarak
t.penup()
t.goto(-25,-250)
t.color("orange")
t.pendown()
t.write("Eid Mubarak",align='center',font=('Jokerman',70,'italic'))
t.color("black")

# Draw stars randomly
t.speed(0)
t.goto(0,250)
t.color("white")
def draw_star():
    turns=6
    t.begin_fill()
    while turns>0:
        t.forward(25)
        t.left(145)
        turns-=1
    t.end_fill()
stars_num=0
while stars_num<20:
    x=randint(-300,300)
    y=randint(100,300)
    draw_star()
    t.penup()
    t.goto(x,y)
    t.pendown()
    stars_num+=1
turtle.exitonclick()