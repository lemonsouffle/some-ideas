import turtle
import random

turtle.bgcolor('black')
turtle.speed(100)
colors = ['red', 'green', 'brown', 'blue', 'white', 'yellow', 'orange', 'gray', 'pink', 'cyan', 'purple']
color = random.choice(colors)
turtle.color(color)
size = random.randint(10, 60)
x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
turtle.penup()
turtle.setpos(x, y)
turtle.pendown()
for j in range(size):
    turtle.forward(2 * j)
    turtle.left(95)

turtle.mainloop()
