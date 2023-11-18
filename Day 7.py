#Hangman

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)

blank_list = []
for _ in range(len(word)):
    blank_list += "_"
    
guessed_letters = 0
lives = 6
print(stages[lives])

while guessed_letters < len(word) and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess not in word:
        lives -= 1
        print(stages[lives])
    else:
        if guess in blank_list:
            print("You have entered it before.")
        else:
            for position in range(len(word)):
                if word[position] == guess:
                    blank_list[position] = guess
                    guessed_letters += 1
            
    print(blank_list)
        
if lives == 0:
    print("You Lose!")
else:
    print("You Win!")
