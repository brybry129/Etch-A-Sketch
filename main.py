from turtle import Turtle, Screen


pointer = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    pointer.forward(10)


def move_backwards():
    pointer.backward(10)


def turn_counter_clockwise():
    pointer.left(10)


def turn_clockwise():
    pointer.right(10)


def clear_drawing():
    pointer.reset()


#main
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="c", fun=clear_drawing)
screen.exitonclick()