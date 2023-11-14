#task.1
import random
random_integer = random.randint(1, 10) #to get random int num from 0 -> 10
print(random_integer)

random_float = random.random()
print(random_float)      #to get random float num from 0 -> 1
print(random_float * 5)  #to get random float num from 0 -> 5



#task.2
random_num = random.randint(0, 1)

if random_num == 0:
    print("Tails")
else:
    print("Heads")



#task.3 => List
cities_of_egypt = ["Alexandria", "Cairo", "Aswan", "Giza"]
print(cities_of_egypt[-1]) #gives last item AND -2 => Aswan ...

cities_of_egypt[1] = "Port said"
print(cities_of_egypt)

cities_of_egypt.append("Cairo")
print(cities_of_egypt)

cities_of_egypt.extend(["Luxor", "Sinai"])
print(cities_of_egypt)



#task.4
names_string = input("Enter your names separated by \", \": ")
names = names_string.split(", ")

#pay_name = random.choice(names)
num_names = len(names)
pay_name = random.randint(0, num_names-1)

print(f"{names[pay_name]} is going to buy the meal today!")



#task.5 => Nested List
list1 = ["A", "B", "C"]
list2 = ["a", "b", "c"]
nested_list = [list1, list2]
print(nested_list)



#task.6
line1 = ["[]", "[]", "[]"]
line2 = ["[]", "[]", "[]"]
line3 = ["[]", "[]", "[]"]

map = [line1, line2, line3]
print(f"     A     B    C\n1 {line1}\n2 {line2}\n3 {line3}")
print("Hiding your treasure! X marks the spot.")
position = input("Where do you wanna put the treasure? ")
pos1 = int(position[1]) - 1
pos2 = position[0].lower()

abc = ["a", "b", "c"]
pos2 = abc.index(pos2)

map[pos1][pos2] = "X"
print(f"     A     B    C\n1 {line1}\n2 {line2}\n3 {line3}")




#Day.4 Project
game = ["Rock", "Paper", "Scissors"]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f"You chose: {game[your_choice]}")
computer_choice = random.randint(0,2)
print(f"Computer chose: {game[computer_choice]}")

if your_choice == computer_choice:
    print("No one win!")
elif your_choice == computer_choice-1 or your_choice == computer_choice+2:
    print("You lose!")
else:
    print("You win!")












