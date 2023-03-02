from turtle import Turtle
import random

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
        #self.trajectory = random.randint(0,359)
        self.trajectory = 240
        self.seth(self.trajectory)
    
    
    def move(self):
        self.fd(2)
        
    def bounce(self):
        if self.ycor() <= BOTTOM or self.ycor() >= TOP:
            new_h = 360 - self.heading()
            self.seth(new_h)
        