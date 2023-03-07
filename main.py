import random
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
net.goto(0, 260)
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
screen.onkeypress(key="W", fun=l_paddle.up)
screen.onkeypress(key="S", fun=l_paddle.down)
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)

scoreboard = Scoreboard()
ball = Ball()

speed = 1.5
game_on = True
while game_on:
    #Sleeps to limit game speed, updates screen
    sleep(0.01)
    screen.update()
    # moves ball by amount specified by speed, checks if ball has collided with wall
    ball.move(speed)
    ball.wall_collision()
    
    #checks if ball has collided with paddle. if true: calls paddle collision
    if ball.distance(l_paddle) < 50 and ball.xcor() < -334 or ball.distance(r_paddle) < 50 and ball.xcor() > 334:
        ball.paddle_collision()
    
    #Handles if player misses the ball, other player gets point, serves ball
    if ball.xcor() > 344:
        scoreboard.inc_score("left")
        ball.goto(-320,0)
        options = [random.randint(0, 40), random.randint(320, 360)]
        choice = random.randint(0,1)
        ball.seth(options[choice])
        if speed < 5:
            speed += 0.5
    if ball.xcor() < -344:
        scoreboard.inc_score("right")
        ball.goto(320,0)
        new_head = random.randint(140, 220)
        ball.seth(new_head)
        if speed < 5:            
            speed += 0.5
       
    #if one player reaches 10 points, ends game
    if scoreboard.l_score >= 10 or scoreboard.r_score > 10:
        scoreboard.game_over()


screen.exitonclick()
