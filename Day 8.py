# def greet(name, location):
#     print(f"Hello {name}!")
#     print(f"What is it like in {location}?")

# greet("Mariam", "El Max")
# greet(location = "El Max", name = "Mariam")

#------------------------------------------------------------------------

# import math

# def paint_calc(cover, height, width):
#     number_of_cans = math.ceil( (height*width)/cover )
#     print(f"You'll need {number_of_cans} cans of paint.")

# test_h = int(input("height of wall: "))
# test_w = int(input("width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#------------------------------------------------------------------------

# def prime_checker(number):
#     is_prime = True
#     if number == 1:
#         is_prime = False
#     for i in range(2, number):
#         if number%i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")


# n = int(input("Check this number: "))
# prime_checker(number=n)

#------------------------------------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def process_fun(prcs, msg, shift):
    new_msg = ""
    for letter in msg:
        new_letter = letter
        if letter in letters:
            new_letter_pos = letters.index(letter) + shift
            if new_letter_pos > 25:
                new_letter_pos -=25

            elif new_letter_pos < 0:
                new_letter_pos +=25
            new_letter = letters[new_letter_pos]
            
        new_msg += new_letter
    print(f"Here is the {prcs} result: {new_msg}")


go_agin = "yes"
while go_agin == "yes":
    process = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift_num = int( input("Type the shift number:\n") )

    if process == "decode":
        shift_num *= -1
    process_fun(prcs = process, msg = message, shift = shift_num)
 
    
    go_agin = input("Type 'yes' if you wanna go again. Otherwise type 'no'\n").lower()
