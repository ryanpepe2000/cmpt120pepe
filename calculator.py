# calculator.py
# CMPT 120
# Date Created: 2018-09-28
# Author: Ryan Pepe

from operator import *

def main():
    equation = str(input("Enter an equation with any basic arithmetic operator: "))

    # Turns user's input into a list of each number and arithmetic operator, regardless
    # of whether the user inputted spaces in between operators.
    equationList = equation.replace("+", " + ").replace("*"," * ").replace("/"," / ").split()

    # Creates blank lists that for each operation and the solution.
    first= []
    second = []


    
    solution = []
    
    order(equationList, first, second)

    print(equationList)
    
    multDiv(equationList)
    addSub(equationList)
    


## Function that marks the location of each arithmetic operator in seperate lists

def order(equation, first, second):
    for i, e in enumerate(equation):
        if e == "*" or e == "/":
            first.append(i)

    for i, e in enumerate(equation):
        if e == "+" or e == "-":
            second.append(i)
            

def multDiv(eq):
    while "*" in eq or "/" in eq:
        for i, e in enumerate(eq):
            if e == "*":
                eq[i] = float(eq[i-1]) * float(eq[i+1])
                del eq[i+1],eq[i-1]
            elif e == "/":
                eq[i] = float(eq[i-1]) / float(eq[i+1])
                del eq[i+1],eq[i-1]
    print(eq)
            
def addSub(eq):
    while "+" in eq or "-" in eq:
        for i, e in enumerate(eq):
            if e == "+":
                eq[i] = float(eq[i-1]) + float(eq[i+1])
                del eq[i+1],eq[i-1]
            elif e == "-":
                eq[i] = float(eq[i-1]) - float(eq[i+1])
                del eq[i+1],eq[i-1]
    print(eq)






















main()


