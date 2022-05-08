# Извлекаем цвета из картинки делаем палитру

# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract("pic_cologram.jpg", 30)    # выделяем 30 цветов
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)  # извлекает цвет rgb
#
# print(rgb_colors)
from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
t.colormode(255)
color_list = [(180, 182, 187), (236, 231, 235), (192, 178, 167), (241, 249, 246), (191, 190, 195), (36, 109, 149), (174, 76, 25), (227, 212, 95), (194, 157, 19), (211, 75, 108), (197, 161, 173), (161, 54, 105), (29, 132, 77), (129, 183, 147), (50, 24, 16), (221, 80, 61), (28, 36, 53), (148, 16, 73), (67, 11, 50), (46, 172, 121), (10, 104, 52), (21, 42, 37), (221, 169, 184), (44, 160, 180), (45, 49, 119), (159, 30, 15), (232, 176, 158), (105, 88, 2)]
tim.hideturtle()
tim.speed("fastest")
tim.setheading(255)
tim.penup()
tim.forward(250)
tim.penup()
tim.setheading(0)

def forward ():
    for _ in range(10):
        point = tim.dot(20, random.choice(color_list))   # рисует точки
        tim.penup()
        tim.forward(50)
        tim.pendown()
for _ in range(10):
    forward ()
    tim.penup()
    tim.back((5*10)+(50*9))
    tim.pendown()
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.pendown()
    tim.right(90)


screen = Screen()
screen.exitonclick()