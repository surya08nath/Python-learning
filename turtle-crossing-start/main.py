import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
cars=CarManager()
score=Scoreboard()


screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
count=1
while game_is_on:
    count+=1
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        score.increase_level()


screen.exitonclick()
    
        

