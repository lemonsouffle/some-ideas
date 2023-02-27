import turtle
import random


def spiral(size):
    for j in range(size):
        turtle.forward(2 * j)
        turtle.left(95)


def star(size):
    turtle.right(random.randint(0, 180))
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)


turtle.bgcolor('black')
turtle.speed(100)
colors = ['red', 'green', 'brown', 'blue', 'white', 'yellow', 'orange', 'gray', 'pink', 'cyan', 'purple']

for i in range(50):
    turtle.color(random.choice(colors))

    turtle.penup()
    x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
    y = random.randint(-turtle.window_height() // 2, turtle.window_height() // 2)
    turtle.setpos(x, y)
    turtle.pendown()

    size = random.randint(10, 60)
    # spiral(size)
    star(size)

turtle.mainloop()
