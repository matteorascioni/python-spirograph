from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

t = Turtle()
t.speed("fastest")
t.hideturtle()

def random_color():
    """ This function produce a tuple with 3 number inside as a output """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    """ This function draw a spirograph """

    #Here we calculate the len of the loop by dividing the usal lenght of a circle by the size_of_gap that each circle has
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

draw_spirograph(5)
screen.exitonclick()