# import colorgram
# rgb_Color = []
# colors = colorgram.extract("images.jpg",30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     New_Color = (r, g, b)
#     rgb_Color.append(New_Color)
#
#
# print(rgb_Color)
import turtle as turtle_module
import random
tim =turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
Color_List = [ (107, 109, 128), (141, 141, 154), (236, 214, 225),
               (223, 211, 116), (175, 73, 37), (203, 148, 174),
               (219,  233, 222), (178, 157, 43), (106, 112, 168), (187, 15, 4), (16, 18, 59), (16, 33, 17), (226, 169, 195), (33, 32, 15), (213, 83, 60), (233, 173, 161), (192, 10, 19), (42, 45, 114), (154, 168, 157), (140, 77, 88), (89, 104, 93), (181, 181, 218), (202, 79, 92), (33, 17, 32), (223, 210, 20), (72, 76, 40), (179, 200, 182)]
tim.setheading(230)
tim.forward(280)
tim.setheading(0)

for dot_count in range(1, 101):
    tim.dot(20, random.choice(Color_List))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
