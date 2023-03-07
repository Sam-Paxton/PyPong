from turtle import Turtle
import random
from paddle import Paddle

TOP = 300
BOTTOM = -300
LEFT = -400
RIGHT = 400

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=1)
        self.trajectory = random.randint(140,220)
        self.seth(self.trajectory)
    
    
    def move(self, speed):
        '''Params: speed : int 
        Moves ball forward by this number of pixels.
        No return'''
        self.fd(speed)
        
    def wall_collision(self):
        '''No Params.
        Checks if ball has collided with wall. if true: reflects heading of ball perpendicular to the wall.
        No return.'''
        if self.ycor() <= BOTTOM or self.ycor() >= TOP:
            new_h = 360 - self.heading()
            self.seth(new_h)
            
    def paddle_collision(self):
        '''No Params.
        Checks if ball has collided with paddle. if true: reflects heading of ball perpendicular to the wall.
        No return.'''
        new_h = (180 - self.heading()) 
        self.seth(new_h)
        