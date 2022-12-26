from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def forward():
    t.forward(10)


def backward():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def reset():
    t.clear()
    t.pu()
    t.home()
    t.pd()


screen.listen()

screen.onkey(key="a", fun=turn_left)
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()
