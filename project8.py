'''This program draws a fractal tree'''

import turtle
from random import randint

#setting the main paramets
t = turtle.Turtle()
t.color('magenta')
t.screen.bgcolor('black')
t.left(90)
tree_level = 13
branch_length = 120
angle = randint(0, 45)

t.width(tree_level)

t.penup()
t.back(branch_length)
t.pendown()
t.forward(branch_length)

def draw_tree(branch_length, level):
    '''This function draws the main tree'''
    width = t.width()  # save the current pen width
    t.width(width * 3 / 4)  # narrow the pen width
    branch_length = 3 / 4 * branch_length
    t.left(angle)
    t.forward(branch_length)

    if level < tree_level:
        draw_tree(branch_length, level + 1)
    t.back(branch_length)
    t.right(2 * angle)
    t.forward(branch_length)

    if level < tree_level:
        draw_tree(branch_length, level + 1)
    t.back(branch_length)
    t.left(angle)

    t.width(width)  # restore the previous pen width

t.speed("fastest")
draw_tree(branch_length, 2)
turtle.done()
