import turtle
import random

turtle.bgcolor('black')
turtle.speed(100)
colors = ['red', 'green', 'brown', 'blue', 'white', 'yellow', 'orange', 'gray', 'pink', 'cyan', 'purple']
color = random.choice(colors)
turtle.color(color)
size = random.randint(10, 60)
for j in range(size):
    turtle.forward(2 * j)
    turtle.left(95)

turtle.mainloop()
