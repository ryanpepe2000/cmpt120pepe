# calculator.py
# CMPT 120
# Date Created: 2018-09-28
# Author: Ryan Pepe

from operator import *

def main():
    equation = str(input("Enter an equation with any basic arithmetic operator: "))

    # Turns user's input into a list of each number and arithmetic operator, regardless
    # of whether the user inputted spaces in between operators.
    equationList = equation.replace("+", " + ").replace("- "," - ").replace("*"," * ").replace("/"," / ").split()

    # Creates blank lists that for each operation and the solution.
    first = []
    second = []

    solution = []
    
    order(equationList, first, second)
    print(first)
    print(second)
    print()

## Function that marks the location of each arithmetic operator in seperate lists
def order(equation, first, second):
    for i, e in enumerate(equation):
        if e == "*" or e == "/":
            first.append(i)
    for i, e in enumerate(equation):
        if e == "+" or e == "-":
            second.append(i)



            
        























main()


