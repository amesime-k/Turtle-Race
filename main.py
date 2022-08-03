import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = turtle.textinput(title="Make a bet", prompt="Which turtle will win the race. Enter color: ")
colors = ["red", 'yellow', 'orange', 'green', 'blue']
all_turtles = []
y = -100
race_is_on = False
for color in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[color])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 40
    all_turtles.append(new_turtle)

if user_input:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_is_on = False
            if user_input == turtle.pencolor():
                print(f"You win. The {turtle.pencolor()} turtle won the race")
            else:
                print(f"You lost. The {turtle.pencolor()} turtle won the race")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
