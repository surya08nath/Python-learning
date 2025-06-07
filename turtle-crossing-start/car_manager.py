COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):  
        self.all_cars=[]
        self.carspeed=STARTING_MOVE_DISTANCE
    
    def create_car(self):
        chance=random.randint(1,6)
        if chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
        # self.shapesize(stretch_len=3,stretch_wid=1)
        # self.color(random.choice(COLORS))
        # self.penup()
        # self.y_cor=random.randint(-250,250)
        # self.goto(300,self.y_cor)
        # self.all_cars.append(new)
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.carspeed)
    
    def level_up(self):
        self.carspeed+=MOVE_INCREMENT


