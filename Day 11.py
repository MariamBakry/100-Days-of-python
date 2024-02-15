import random
import sys

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def display_hands():
    print(f"Computer: {computer}, current score: {sum(computer)}")
    print(f"User: {user}, current score: {sum(user)}")

def end_game(user_score, computer_score):
    display_hands()
    if computer_score > 21 and user_score <= 21:
        print("you win")
    elif user_score > 21 or computer_score > user_score:
        print("you lose")
    elif user_score == 21 or user_score > computer_score:
        print("you win")
    elif user_score == computer_score:
        print("Draw")
    sys.exit(0)

def blackjack():
    if sum(computer) == 21:
        print("Computer Blackjack, you lose")
        sys.exit(0)
    elif sum(user) == 21:
        print("User Blackjack, you win")
        sys.exit(0)

        
def draw_card(player):
    card = deal_card()
    if card == 11 and sum(player) > 10:
        card = 1
    player.append(card)
    if sum(player) == 21:
        end_game(sum(user), sum(computer))
        
    elif sum(player) > 21:
        if 11 in player:
            player.remove(11)
            player.append(1)
        else:
            end_game(sum(user), sum(computer))


computer = [deal_card(), deal_card()]
user = [deal_card(), deal_card()]

user_score = sum(user)
computer_score = sum(computer)

print(f"Computer: [{computer[0]}, ?]")
print(f"User: {user}, current score: {user_score}")

if user_score > 21 or computer_score > 21:
    end_game(user_score, computer_score)
blackjack()

flag = 'y'
flag = input("if you want a card press y otherwise press n: ")

while flag == 'y' and sum(user) < 21:
    draw_card(user)
    user_score = sum(user)
    print(f"User: {user}, current score: {user_score}")
    flag = input("if you want a card press y otherwise press n: ")

display_hands()
while True:
    draw_card(computer)
    computer_score = sum(computer)
    if computer_score >= 17:
        break
    display_hands()
    
end_game(user_score, computer_score)
