import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
tim = Player()
cars = CarManager()
screen.onkey(tim.move_forward, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_cars()
    cars.move_car()

    #detect collision with car
    for i in cars.all_cars:
        if i.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect succesful crossing
    if tim.crossed_finishing():
        tim.go_to_start()
        cars.level_up()
        scoreboard.level_up()
        scoreboard.print_level()

screen.exitonclick()
