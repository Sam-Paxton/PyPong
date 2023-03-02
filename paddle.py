from turtle import Turtle

LEFT = (-350,0)
RIGHT = (350,0)

class Paddle(Turtle):
    
    def __init__(self, position):
        '''
        '''
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.speed("fast")
        self.pu()
        if position == "left":
            self.goto(LEFT)
        if position == "right":
            self.goto(RIGHT)
        self.shapesize(stretch_wid=5, stretch_len=0.3)
    
    def up(self):
        print(f"{self.position} paddle UP")
        self.goto(self.xcor(), self.ycor()+30)
        
    def down(self):
        print(f"{self.position} paddle DOWN")
        self.goto(self.xcor(), self.ycor()-30)
        
        
        
    