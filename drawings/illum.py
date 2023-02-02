import math
import turtle
from turtle import *
#prompt is to "Sample a color palette from your favorite movie/album cover"
#chosen album cover inspiration is one hundred mornings by windows96 
#=================draw bg gradient================
turtle.title("One hundred mornings palette")
turtle.hideturtle()
color = (1, 1, 1)  # (154, 0, 254)
target = (0.38, 0.55, 0.84)  #RGB(98, 141, 214)

tur = Screen()
tur.tracer(False)

width, height = tur.window_width(), tur.window_height()
deltas = [(hue - color[index]) / height for index, hue in enumerate(target)]
bg = Turtle()
bg.color(color)
bg.penup()
bg.goto(-width/2, height/2)
bg.pendown()
direct = 1
for distance, y in enumerate(range(height//2, -height//2, -1)):
    bg.forward(width * direct)
    bg.color([color[i] + delta * distance for i, delta in enumerate(deltas)])
    bg.sety(y)
    direct *= -1
tur.tracer(True)

#=========================helper functions==================================
def draw_rect(t, x, y, xx, yy, width):
    t.goto(x, y)
    t.setheading(t.towards(xx, yy))
    t.begin_fill()
    for d in [t.distance(xx, yy), width] * 2:
        t.forward(d)
        t.left(90)
    t.end_fill()

def draw_shape(t, r, n, colors, dir_offset):
    for i in range(n + 1):
        a = 360 / n * (i + dir_offset)
        t.color(colors[i%len(colors)])
        t.begin_fill()
        t.goto(0, 0)
        x = math.cos(math.radians(a)) * r
        y = math.sin(math.radians(a)) * r
        t.goto(x, y)
        t.end_fill()

def draw_lines(t, r, n, bold, dir_offset):
    for i in range(n):
        a = 360 / n * (i + dir_offset)
        x = math.cos(math.radians(a)) * r
        y = math.sin(math.radians(a)) * r
        a = 360 / n * (1 + i + dir_offset)
        xx = math.cos(math.radians(a)) * r
        yy = math.sin(math.radians(a)) * r
        draw_rect(t, x, y, xx, yy, bold)

#======================first shape==============================
shape = turtle.Turtle()
shape.hideturtle()
shape.screen.setup(width, height)

shape.penup()
shape.speed("fastest")
sides = 4  
bold=10
draw_shape(shape, 350, sides, ["#BC9773", "#C8AD7F", "#804e20"],0.5)
shape.color("#4CBE72")

#======================second shape==============================
shape2=turtle.Turtle()
shape2.hideturtle()
shape2.penup()
shape2.speed("fastest")
sides2 = 30
bold=3
draw_shape(shape2, 250, sides, ["#728C69", "#B2D3C2", "#597D35"],0.5)
shape2.color("#4F6137")




#======================driver code==============================

for i in range(50, 300, 100):
    draw_lines(shape, i, sides, bold,0.5)

shape.ht()
turtle.exitonclick()