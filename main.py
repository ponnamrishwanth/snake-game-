from sanke import Snake
import time
from turtle import Screen
from food import Food
from scorecard import Scorecard
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my sanke game")
screen.tracer(0)
screen.listen()
food = Food()
snake=Snake()
scorecard=Scorecard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
is_game_on= True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorecard.new_score()
    if snake.head.xcor() > 290 or snake.head.xcor()<-290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        scorecard.reset()
        snake.reset_snake()
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            scorecard.reset()
            snake.reset_snake()
screen.exitonclick()