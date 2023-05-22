import time
from Player import Player
from Scoreboard import Scoreboard
from Roads import *

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle: Cross the Road")
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
cars = Car()


screen.listen()
screen.onkey(key="Up", fun=player.go_forward)
screen.onkey(key="Left", fun=player.go_left)
screen.onkey(key="Right", fun=player.go_right)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move()

    # Detect collisions with car
    for car in cars.all_cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing - Reach finish line
    if player.ycor() >= 280:
        cars.level_up()
        scoreboard.score_point()
        player.go_to_start()







screen.exitonclick()