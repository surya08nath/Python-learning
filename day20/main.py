from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.moveup,"Up")
screen.onkey(snake.moveright,"Right")
screen.onkey(snake.moveleft,"Left")
screen.onkey(snake.movedown,"Down")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()

    
   

        





screen.exitonclick()