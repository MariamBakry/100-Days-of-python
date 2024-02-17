# # turtle is a graphic package and Turtle, Screen are classes
# from turtle import Turtle, Screen

# #object of Turtle class(used for drawing graphics)
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# #object of Screen class(used for creating a screen for the graphics)
# my_screen = Screen()
# print(my_screen)

# #to make the screen get closed by clicking on it(without calling exitonclick() method the screen will close immediately by it self)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

#align is an attribute on the method set_style that can be used like this to change the style of the table th be aligned in the left 'l', right 'r', center 'c'(by default)
table.align = "l"
print(table)
