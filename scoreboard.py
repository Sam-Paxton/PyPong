from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        '''No parameters.
            Creates scoreboard at top of Screen. Starts at 0.
        '''
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,260)
        self.write_score()
        
        
    def inc_score(self, side : str):
        '''increment=1 by default.
            Adds increment to score.
            No return.
        '''
        if side == "left":
            self.l_score += 1
        elif side == "right":
            self.r_score += 1
        self.clear()
        self.write_score()
        
    def write_score(self):
        '''No parameters.
            Writes score to scoreboard.
            No return.
        '''
        content = f"{self.l_score}   FIRST TO 10 WINS    {self.r_score}"
        self.write(arg=content,
                   move=False,
                   align="center",
                   font=('Arial',24,"bold")
                   )
        
    def game_over(self):
        '''No parameters.
            Writes 'GAME OVER' to centre of screen.
            No return.'''
        self.clear()
        self.write(arg=f"{self.l_score}      GAME OVER       {self.r_score}", align="center", font="Arial")