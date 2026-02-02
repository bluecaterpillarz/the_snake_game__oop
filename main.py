import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

screen.update()

game_on=True

while(game_on):
    screen.update()
    time.sleep(0.1)
    snake.snake_forward()
    if snake.turtles[0].distance(food) < 15:
        food.appear()
        scoreboard.score += 1
        scoreboard.score_refresh()
        snake.getting_bigger()
    if snake.turtles[0].xcor()>280 or snake.turtles[0].xcor()<-280 or snake.turtles[0].ycor()>280 or snake.turtles[0].ycor()<-280:
        game_on=False
        scoreboard.game_over()
    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle)<10:
            scoreboard.game_over()
            game_on=False

















screen.exitonclick()