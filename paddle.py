from turtle import Turtle

LEFT = (-350,0)
RIGHT = (350,0)

class Paddle(Turtle):
    
    def __init__(self, position):
        '''Param: str either 'left' or 'right' to place
            the paddle on the screen
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
        '''No params.
            Move paddle up 50 pixels.
            No Return.
        '''
        self.goto(self.xcor(), self.ycor()+50)
        
    def down(self):
        '''No params.
            Move paddle up 50 pixels.
            No Return.
        '''
        self.goto(self.xcor(), self.ycor()-50)
    
        
        
        
    