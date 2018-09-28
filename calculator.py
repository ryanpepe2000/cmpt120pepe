# calculator.py
# CMPT 120
# Date Created: 2018-09-28
# Author: Ryan Pepe

def main():
    equation = str(input("Enter an equation with any basic arithmetic operator: "))

    # Turns user's input into a list of each number and arithmetic operator, regardless
    # of whether the user inputted spaces in between operators.
    equationList = equation.replace("+", " + ").replace("-"," - ").replace("*"," * ").replace("/"," / ").split()

    
    
main()
