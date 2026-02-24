import math
import turtle





t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pensize(2)



t.color("red")

def heart_point(a):
    x = 15 * math.sin(a) ** 3
    y = (
        12 * math.cos(a)
        - 5 * math.cos(2 * a)
        - 2 * math.cos(3 * a)
        - math.cos(4 * a)
    )
    return x * 15, y * 15

center = (0, 0)

for i in range(360):
    ang = math.radians(i)
    x, y = heart_point(ang)
    t.penup()
    t.goto(center)
    t.pendown()
    t.goto(x, y)





turtle.done()
