import random
import turtle

from random_color import random_color

t = turtle.Turtle()


def draw_star(x, y):
    t.penup()
    t.goto(x, y)
    # Set the random color of the star
    t.color(random_color())
    t.pendown()
    # Set the random size of the star
    size = random.randint(1, 200)
    for i in range(5):
        t.forward(size)
        t.right(144)


s = turtle.Screen()
# call the function draw_star when the mouse is clicked
s.onscreenclick(draw_star)
turtle.done()
