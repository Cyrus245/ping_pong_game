from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title('Ping Pong Game')
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# event listener
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed('fastest')

    # detection of which player misses
    # if right player misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_pont()

    # if left player misses
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
