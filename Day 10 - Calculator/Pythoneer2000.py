# Import Logo
from Calculator_art import logo

# Define the basic functions of the calculator
def add(n1,n2):
    return n1 + n2
def subtraction(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

# Create a dictionary the binds a key with the operations/values
operations = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": divide,
}
# Defining the whole calculator as a function we can use Recursion - Calling it once more if the user wants to clear the saved numbers
def calculator():
    print(logo)
    # Asks for the first number and transforms it to float so decimal numbers can be used in calculations
    num1 = float(input("What's the first number?\n"))
    # Loops in to the operations dictionary to print all possible operations for the user to choose from
    for operator in operations:
       print(operator)
    # State a boolean, so we can stop the calculator to keep going and using the last number calculated
    should_continue = True
    while should_continue:
        # Asks what operation the user wants to do
        operation_symbol = input("Pick an operation:\n")
        # Asks for the second number
        num2 = float(input("What's the next number?\n"))
        # Stores wished operator into a variable and goes to the dictionary to find it's key and corresponding value
        calculation_function = operations[operation_symbol]
        # Finally calls the function using the two inputs from above and save it into a new variable
        answer = calculation_function(num1,num2)
        # Print the formed equation and it's answer
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        go_forward = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if go_forward == "y":
            num1 = answer
        elif go_forward == "n":
            # Important to set a Flag for the function to call itself - Otherwise you've a infinite loop
            should_continue = False
            calculator()
        else:
            print("Invalid parameter - Stopping program.")
calculator()