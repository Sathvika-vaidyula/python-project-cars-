from turtle import Screen
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Check if player has reached the finish line
    if player.is_at_finish_line():
        player.goto_start()
        scoreboard.increase_level()

    # Optional condition to simulate game over (e.g., reaching level 5)
    if scoreboard.level > 5:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
