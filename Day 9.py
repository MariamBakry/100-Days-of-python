#student_scores = {
#    "Harry": 81,
#    "Ron": 78,
#    "Hormione": 99,
#    "Draco": 74,
#    "Neville": 62,
#}

#student_grades = {}

#for student in student_scores:
#    score = student_scores[student]
#    if score > 90:
#        student_grades[student] = 'Outstanding'
#    elif score > 80 :
#        student_grades[student] = 'Exceeds Expectations'
#    elif score > 70:
#        student_grades[student] = 'Acceptable'
#    else:
#        student_grades[student] = 'Fail'

#print(student_grades)

##################################################

#country = input("Add country name: ")
#visits = int(input("Enter number of visits: "))
#list_of_cities = eval(input("Enter list of cities that you visit: "))

#travel_log = [
#    {
#        "country": "France",
#        "visits": 12,
#        "cities": ["Paris", "Lille", "Dijon"]
#    },
#    {
#        "country": "Germany",
#        "visits": 5,
#        "cities": ["Berlin", "Hamburg", "Stuttgart"]
#    },
#]

#def add_new_country(country, visits, list_of_cities):
#    new_country = {
#        "country": country,
#        "visits": visits,
#        "cities": list_of_cities
#    }
#    return new_country

#travel_log.append( add_new_country(country, visits, list_of_cities) )
#print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
#print(f"My fav city was {travel_log[2]['cities'][0]}.")

 ###################################################

print("Welcome to the secret auction program!")
bidders = {}
flag = 'yes'

def add_bidder():
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid

def find_highest_bidder():
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while flag == 'yes':
    add_bidder()
    flag = input("Are there any other bidders? Type 'yes' or 'no'").lower()

find_highest_bidder()
