import turtle
import random


def spiral(s):
    for j in range(s):
        turtle.forward(2 * j)
        turtle.left(95)


def star(s):
    turtle.right(random.randint(0, 180))
    for _ in range(5):
        turtle.forward(s)
        turtle.right(144)


def flower(s):
    ang = random.randint(5, 15)
    for _ in range(ang):
        for angle in [60, 120, 60, 120]:
            turtle.forward(s)
            turtle.right(angle)
        turtle.right(360/ang)


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
    # star(size)
    flower(size)
    
turtle.mainloop()
