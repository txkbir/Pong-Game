import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.update()
screen.listen()
screen.onkeypress(fun=r_paddle.up, key='Up')
screen.onkeypress(fun=r_paddle.down, key='Down')
screen.onkeypress(fun=l_paddle.up, key='w')
screen.onkeypress(fun=l_paddle.down, key='s')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with boundaries
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect r_paddle missing
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        r_paddle.reset_paddle()
        l_paddle.reset_paddle()

    # Detect l_paddle missing
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        r_paddle.reset_paddle()
        l_paddle.reset_paddle()

    if score.l_score > 0:
        game_on = False
        continue
    elif score.r_score > 0:
        game_on = False
        continue

screen.exitonclick()
