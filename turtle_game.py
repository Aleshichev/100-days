import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(700, 600)    # размер окна
user_bet = screen.textinput(title="Алиса, выбери цвет:", prompt=" red, orange, yellow, green, blue, purple ")
user_bet2 = screen.textinput(title="Алла, выбери цвет:", prompt=" red, orange, yellow, green, blue, purple ")
user_bet3 = screen.textinput(title="Игорь, выбери цвет:", prompt=" red, orange, yellow, green, blue, purple ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-340, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 320:
            is_race_on = False
            winning_color = turtle.pencolor()   # цвет пера
            if winning_color == user_bet:
                print(f"Алиса выиграла!!!")
            elif winning_color == user_bet2:
                print(f"Алла выиграла!!!")
            elif winning_color == user_bet3:
                print(f"Игорь выиграл!!!")
            else:
                print(f"You've lost! The {winning_color} turtle is win")
        random_distance = random.randint(0,10)
        turtle.forward((random_distance))


screen.exitonclick()
