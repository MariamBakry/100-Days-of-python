#task.1
print("Welcome to the rollercoaster!")
height = int( input("What is your height in cm? ") )

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


#task.2  
num = int( input("Enter any number: ") )

if num%2 == 0:
    print("The number is even!")
elif num%2 ==1:
    print("The number is odd!")



#task.3
height = float( input("Enter your height: ") )
weight = int( input("Enter your weight: ") )
bmi = weight / height **2
message = f"Your BMI is {bmi}, you "
if bmi < 18.5:
    print(message + "are underweight.")
elif bmi < 25:
    print(message + "have a normal weight.")
elif bmi < 30:
    print(message + "are slightly overweight.")
elif bmi < 35:
    print(message + "are obese.")
else:
    print(message + "are clinically obese.")



#task.4
year = int( input("Enter any year: ") )

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("A leap year!")
        else:
            print("Not a leap year!")
    else:
        print("A leap year!")
else:
    print("Not a leap year!")



#task.5
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N?")
extra_cheese = input("Do you want extra cheese? Y or N?")
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
else:
    if size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    if add_pepperoni == "Y":
        bill += 3
    
if extra_cheese == "Y":
    bill += 1

print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")



#task.6
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
combine_names = name1 + name2

e_score = combine_names.count("e")
true_score = love_score = e_score

true_score += combine_names.count("t")
true_score += combine_names.count("r")
true_score += combine_names.count("u")

love_score += combine_names.count("l")
love_score += combine_names.count("o")
love_score += combine_names.count("v")

score = int( str(true_score) + str(love_score) )

print("The Love Calculator is calculating your score...")
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")




#Day 3 project
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

destination = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\" \n").lower()

if destination == "left":
    action = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()
    if action == "wait":
        colour = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if colour == "yellow":
            print("You found the treasure! You Win!")
        elif colour == "red":
            print("It's a room full of fire. Game over!")
        elif colour == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You choose a door that doesn't exist. Game Over!")
    else:
            print("You got attacked by an angry trout. Game over!")
else:
    print("You fell into a hole. Game over!")




