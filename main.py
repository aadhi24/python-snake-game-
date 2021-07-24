import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.title("anaconda game")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
snake = Snake()
foods = Food()
score_t = Score()
game_no = True
times = 0.2
while game_no:
    screen.update()
    time.sleep(times)
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.lefts, "Left")

    if snake.head.distance(foods) < 15:
        foods.refresh()
        snake.extend()
        times -= 0.01
        score_t.current_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_no = False
        score_t.game_over()
    for segment in snake.segment[1:]:

        if snake.head.distance(segment)< 10:
            game_no = False
            score_t.game_over()
    if score_t.scores >=5 and score_t.scores <10 :
        screen.bgcolor("green")
screen.exitonclick()
