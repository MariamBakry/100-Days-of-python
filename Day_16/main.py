# turtle is a graphic package and Turtle, Screen are classes
from turtle import Turtle, Screen

#object of Turtle class(used for drawing graphics)
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

#object of Screen class(used for creating a screen for the graphics)
my_screen = Screen()
print(my_screen)

#to make the screen get closed by clicking on it(without calling exitonclick() method the screen will close immediately by it self)
my_screen.exitonclick()
