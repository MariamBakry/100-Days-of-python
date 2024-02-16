from game_data import data
from art import logo, vs
import random
import os

score = 0

def clear(): # to clear the screen and print the game logo
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
    print(logo)

def get_compare_b(compare_a):
    compare_b = random.choice(data)
    if compare_b['follower_count'] == compare_a['follower_count']: #to avoid two accounts with the same number of followers
        return get_compare_b(compare_a) #if this statement happened then get a new compare_b 
    data.remove(compare_b)
    return(compare_b)

def print_comparables(compare_a, compare_b):
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")

def max_followers(compare_a, compare_b):
    if compare_a['follower_count'] > compare_b['follower_count']:
        return('A')
    elif compare_a['follower_count'] < compare_b['follower_count']:
        return('B')

def new_level(compare_a):
    global score
    if score > 0: # if user get new score and he is not in the beginning of the game
        clear()
        print(f"You're right! Current score: {score}.")
        
    compare_b = get_compare_b(compare_a)
    print_comparables(compare_a, compare_b)
    
    answer = max_followers(compare_a, compare_b) #the right answer
    user_answer = input("How has more followers? Type 'A' or 'B': ")

    if user_answer == answer:
        score +=1
        return new_level(compare_b) #recursion for new level
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
     
def game():
    clear()
    compare_a = random.choice(data)
    data.remove(compare_a) # to avoid repeat it
    new_level(compare_a)
    
game()
