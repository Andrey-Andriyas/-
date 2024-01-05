# from turtle import *

# my_turtle = Turtle()
# my_turtle.speed(0)
# my_turtle.screen.setup(800, 800)

# # Нарисовать квадрат
# def draw_rect(t):
#     for x in range(0, 4):
#         t.right(90)
#         t.forward(100)

# # Рисует квадраты в цикле
# for x in range(0, 360):
#     draw_rect(my_turtle)
#     my_turtle.right(1)


#my_turtle.fd(200) --движение черепашки вправо


#Черепашка рисует пунтирную линиб
# for i in range(20):  
#     my_turtle.fd(8)
#     my_turtle.up()
#     my_turtle.fd(8)
#     my_turtle.down()


#Черепашка рисует прямоугольник
# def rectangle(w, h):
#     for i in range(2):
#         my_turtle.left(90)
#         my_turtle.fd(h)
#         my_turtle.left(90)
#         my_turtle.fd(w)        
# rectangle(320, 200)    


#C помощью черепашки рисуется квадрат и вписанная в него окружность

# def sq_cr(side):
#     for i in range(4):
#         my_turtle.left(90)
#         my_turtle.fd(side)
#     my_turtle.bk(side / 2)
#     my_turtle.circle(side / 2, 360)
#     my_turtle.left(180)
#     my_turtle.circle(side / 2, 360)
# sq_cr(250)


#Рисование круга с заданным количеством точек на нем
# def circ(d, r, rBig):
#     for i in range(d):
#         my_turtle.circle(rBig, 360 / d)
#         my_turtle.dot(r, "blue")
# my_turtle.up()
# my_turtle.goto(350, 0)
# my_turtle.setheading(90)
# my_turtle.down()
# circ(45, 10, 350)


#Программа рисует волны, закрашивается только верхняя часть этих волн.

# my_turtle.up()
# my_turtle.goto(-450, 0)
# my_turtle.down()
# my_turtle.setheading(270)
# for i in range(5):
#     my_turtle.circle(50, 180)
#     my_turtle.begin_fill()
#     my_turtle.circle(-50, 180)
#     my_turtle.end_fill() 


#Черепашка оставляет след синего цвета, затем рисует дугу
# my_turtle.shape("turtle")
# my_turtle.color("blue")
# my_turtle.stamp()
# my_turtle.color("black")
# my_turtle.up()
# my_turtle.fd(50)
# my_turtle.down()
# my_turtle.circle(200, 70)


#Задаём оранжевый цвет заднего фона.
# my_turtle.screen.bgcolor("orange")


# Необходимо, чтобы окно не закрывалось само, а только по клику
# my_turtle.screen.exitonclick()
# my_turtle.screen.mainloop()


# Простейший рисунок медведя
import turtle

t = turtle.Turtle()
t.speed(2)

# Голова
t.penup()
t.goto(0, -100)  # Перемещаемся в центр головы
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.circle(100)  # Рисуем круг для головы
t.end_fill()

# Левое ухо
t.penup()
t.goto(-70, 80)  # Перемещаемся в позицию над левым ухом
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.circle(40)  # Рисуем круг для уха
t.end_fill()

# Правое ухо
t.penup()
t.goto(70, 80)  # Перемещаемся в позицию над правым ухом
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.circle(40)  # Рисуем круг для уха
t.end_fill()

# Левый глаз
t.penup()
t.goto(-35, 40)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(10)
t.end_fill()

# Правый глаз
t.penup()
t.goto(35, 40)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(10)
t.end_fill()

# Нос
t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(20)
t.end_fill()

#Рот
t.penup()
t.goto(-50, -20)
t.pendown()
t.width(5)
t.right(90)
t.circle(50, 180)
t.hideturtle()

turtle.done()



