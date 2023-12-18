#def format_name(f_name, l_name):
#    #DOCString (we use it as a documentaion of the function, when we call the function and let the mouse on it, it will appear)
#    """Take a first and last name and format it
#    to return the title case version of the name."""
#    if f_name == "" or l_name == "":
#        return "You didn't provide valid inputs."
#    f_name = f_name.title()
#    l_name = l_name.title()
#    return f"{f_name} {l_name}"
#print(format_name(input("What is your first name? "), input("What is your last name? ")))
#################################################

#def is_leap(year):
#    leap = False
#    if year%4 == 0:
#        if year%100 == 0:
#            if year%400 == 0:
#                leap = True
#        else:
#            leap = True
#    return leap

#def days_in_month(year, month):
#    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#    if is_leap(year) and month == 2:
#        return 29
#    return month_days[month-1]

#year = int(input("Enter a year: "))
#month = int(input("Enter a month: "))
#days = days_in_month(year, month)
#print(f"{days} days")
###################################################

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_continue = "y"
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
        
    while should_continue == "y":
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")

        if should_continue == "y":
            num1 = answer
        else:
            calculator() #Recursion

calculator()
