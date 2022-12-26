from turtle import Turtle, Screen
import random

game_on = True
colors = ["Purple", "Blue", "Green", "Orange", "Red"]
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=500)
initial_y = [100, 50, 0, -50, -100]
champions = []
for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.pu()
    t.color(colors[i])
    t.goto(-230, initial_y[i])
    champions.append(t)

bet = screen.textinput(title="BET", prompt="Write the color of the turtle you will bet on: ").lower()
if bet:
    game_on = True

while game_on:

    for i in champions:
        if i.xcor() > 230:
            winner = i.fillcolor()
            if winner.lower() == bet:
                print(f"Congrats, your bid has won the race! The winning color was {winner}")
            else:
                print(f"Sorry, you lost. The winning color was {winner}")
            exit(0)
        dist = random.randint(0, 10)
        i.forward(dist)

screen.exitonclick()
