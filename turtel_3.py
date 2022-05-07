from turtle import Turtle, Screen
import random
import turtle as t
tim = Turtle()

t.colormode(255)

def random_color():
    """Генерирует и возвращает произвольный цвет"""
    r = random.randint(2, 255)
    g = random.randint(2, 255)
    b = random.randint(2, 255)
    color_list = (r, g, b)
    return color_list

tim.pensize(3)
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)     # делает сдвиг круга от текущей позиции на отступ

draw_spirograph(10)
screen = t.Screen()
screen.exitonclick()