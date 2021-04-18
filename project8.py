import turtle
from random import randint
t = turtle.Turtle()
t.screen.bgcolor('black')

t.lt(90)

lv = 13
l = 120
s = int (randint(0, 45))

t.width(lv)

t.penup()
t.bk(l)

t.pendown()
t.fd(l)
color = [0.35, 0.2, 0.0]

def draw_tree(l, level):
    width = t.width()  # save the current pen width

    t.width(width * 3.0 / 4.0)  # narrow the pen width
    t.color(color)
    l = 3.0 / 4.0 * l

    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.rt(2 * s)
    t.fd(l)
    color[1] += 0.04

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.lt(s)

    t.width(width)  # restore the previous pen width

t.speed("fastest")

draw_tree(l, 2)

turtle.done()