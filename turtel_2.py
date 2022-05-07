from turtle import Turtle, Screen
import random
import turtle as t
tim = Turtle()
tim.shape("turtle")
tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# tim.color("green")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)

colours = ["antique white", "goldenrod", "yellow", "spring green", "dark magenta",
           "light coral", "lawn green", "rosy brown", "dark violet", "gold"]
directions = [0, 90, 180, 270]
tim.speed(15)
tim.pensize(15)
t.colormode(255)

def random_color():
    """Генерирует и возвращает произвольный цвет"""
    r = random.randint(2, 255)
    g = random.randint(2, 255)
    b = random.randint(2, 255)
    color_list = (r, g, b)
    return color_list



for _ in range (200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)
#         num_side += 1
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)










screen = Screen()
screen.exitonclick()