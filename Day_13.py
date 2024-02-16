############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): ###########the bug is 20 is not included in the range
#     if i == 20:
#       print("You got it")
# my_function()

## solu
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

#############################################

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) ###########the bug is there is no index = 6
# print(dice_imgs[dice_num])

## solu
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

##############################################

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: ###########the bug is there is no = condition
#   print("You are a Gen Z.")

## solu
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994: 
#   print("You are a Gen Z.")

#############################################

# # Fix the Errors
# age = input("How old are you?") ###########the bug is int()
# if age > 18:
# print("You can drive at age {age}.")

## solu
# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")

#############################################

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) ###########the bug is ==
# total_words = pages * word_per_page
# print(total_words)

## solu
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

##############################################

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) ###########the bug is the tab (it is out of the for loop)
#   print(b_list)

# mutate([1,2,3,5,8,13])

## solu
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

##############################################
## Which number do you want to check?
# number = int(input())

# if number % 2 = 0: ##########the bug is there is only one =
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

## solu
# number = int(input())

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

##############################################
## Which year do you want to check?
# year = input() ##########the bug is there is no int() function

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

## solu
# year = int(input())

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

#########################################
## FizzBuzz
# target = int(input())
# for number in range(1, target+1):
#     if number % 3 == 0 or number % 5 == 0: ##########the bug is it should be 'and' not 'or'
#         print("FizzBuzz")
#     if number % 3 == 0: ##########the bug is it should be elif
#         print("Fizz")
#     if number % 5 == 0: ##########the bug is it should be elif
#         print("Buzz")
#     else:
#         print([number])

## solu
# target = int(input())
# for number in range(1, target+1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])