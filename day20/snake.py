from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            
    
    def add_segment(self,pos):
        tim=Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def moveup(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def moveright(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def moveleft(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def movedown(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)        