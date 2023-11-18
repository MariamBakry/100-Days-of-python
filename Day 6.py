#functions

def my_function():
    print("Hello")
    print("Bye")
my_function()


#reeborg game Hurdle 4

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_around()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

#while loop (we use it when i don't care how many time i will do it, i just care about reaching the goal)

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()







#Maze

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()












