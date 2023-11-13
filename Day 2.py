#task.1

two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit

print(two_digit_number)


#task.2

height = input()
weight = input()

BMI = int( int(weight) / float(height) ** 2 )

print(BMI)


#task.3

print(8/3)              #2.666666666
print( int(8/3) )       #2
print( round(8/3) )     #3
print( round(8/3, 2) )  #2.67
print(8 // 3)           #2, and the type is int

#f-String :-
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


#task.4

age = int( input( "Enter your age: " ) )
weeks_left = ( 90 - age ) *52
print(f"You have {weeks_left} weeks left.")



#Day.2 project

print("Welcome to the tip calculator.")
bill = float( input( "What was the total bill? $" ) )
tip = int( input( "What percentage tip would you like to give? 10, 12 or 15? " ) )
people = int( input( "How many people to split the bill? " ) )

each_person_pay = round( ( bill + bill * tip / 100 ) / people ,2)
print(f"Each person should pay: ${each_person_pay}")




















