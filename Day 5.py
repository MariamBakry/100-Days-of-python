#task.1
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)



#task.2
student_heights = input("Enter students heights splited by \", \": ").split(", ")
sum_of_heights = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_of_heights += student_heights[n]

avg = round( sum_of_heights/len(student_heights) )
print(f"The average height = {avg}")




#task.3
student_scores = input("Enter students heights splited by space: ").split()
highest_score = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] > highest_score:
        highest_score = student_scores[n]
print(f"Highest score = {highest_score}")



#task.4
for n in range(1, 10):  # 1 2 3 .. 10
    print(n)

for n in range(1, 11, 3):  # 1 4 7 10
    print(n)

total = 0
for n in range(1, 101): # 1 -> 100
    total += n
print(total)



#task.5
target = int(input("Enter you target num between 0 and 100: "))+1
sum = 0
for n in range(2, target, 2):
    sum += n
print(sum)



#task.6
for n in range(1, 101):
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)




#Day.5 Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_letters = int( input("How many letters would you like in your password?\n") )
no_symbols = int( input("How many sumbols would you like?\n") )
no_numbers = int( input("How many numbers would you like?\n") )
password_list = []
password = ""

for n in range(0, no_letters):
    password_list.append( random.choice(letters) )
    
for n in range(0, no_symbols):
    password_list.append( random.choice(symbols) )
    
for n in range(0, no_numbers):
    password_list.append( random.choice(numbers) )

for n in range(0, len(password_list)):
    char = random.choice(password_list)
    password += char
    password_list.remove(char)

#you can also random the order of the list using: random.shuffle(password_list)

print(f"Here is your password: {password}")













