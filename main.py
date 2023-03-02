from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


net = Turtle()
net.ht()
net.pensize(5)
net.penup()
net.pencolor("white")
net.goto(0,300)
net.seth(270)
dashes = 20
for _ in range(dashes):
    down = net.isdown()
    if down:
        net.pu()
    else:
        net.pd()
    net.fd(30)

l_paddle = Paddle(position="left")
r_paddle = Paddle(position="right")

screen.listen()
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)

scoreboard = Scoreboard()

ball = Ball()



game_on=True
while game_on:
    sleep(0.01)
    screen.update()
    ball.move()
    ball.bounce()








screen.exitonclick()