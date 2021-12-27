logo = """
 _____________________
|  _________________  |
| |               . | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|

"""



# Welcome to the calculator app!
while True: # meant to be used until quit() is used

    print("Welcome to Simple Calculator.py ! ")
    print(logo)
    # we need to define addition, subtraction, multiplication, division

    def add(a, b): # addition
        answer = a + b
        return(answer)

    def minus(a, b): #subtraction
        answer = a - b
        return(answer)

    def mutiply(a, b): # multiplication
        answer = a * b
        return(answer)

    def divide(a, b): # division
        answer = a / b
        return(answer)


    # Make a dictionary with the operators and keys
    operators = {
    "+" : add,
    "-" : minus,
    "*": mutiply,
    "/" : divide
    }


    # get a first and a second number

    a = int(input("What is the first number?")) # First number


    for o in operators:  # print out the operators
        print(o)

    operator_symbol = input("what operator are we going to use?") # operators are +,-,*, and /
    # now use the first number with the operator and second number

    b = int(input("what is the second number")) # second number

    calculationfunction = operators[operator_symbol] # the calculating function is the same as an operators and we use the operator_symbol to reference
    # the operators dictionary


    answer = calculationfunction(a, b) # answer equals the calculating function and using the a and b arguements.

    print(f"{a} {operator_symbol} {b} = {answer} \n " )  # printing a with the operator_symbol and b to get the answer
