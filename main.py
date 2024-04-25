import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_speed = 0.2
game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    car_manager.generate_car()
    car_manager.move_car()

    # Detect collision with finished line
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.refresh_score()
        game_speed *= 0.7

    # Detecting collision with car
    for car in car_manager.cars[0:]:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
