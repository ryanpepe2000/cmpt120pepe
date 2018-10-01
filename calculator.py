# calculator.py
# CMPT 120
# Date Created: 2018-09-28
# Author: Ryan Pepe

from operator import *

def main():
    equation = str(input("Enter an equation with any basic arithmetic operator: "))

    # Turns user's input into a list of each number and arithmetic operator, regardless
    # of whether the user inputted spaces in between operators.
    equationList = equation.replace("+", " + ").replace("-"," - ").replace("*"," * ").replace("/"," / ").split()

    # Creates blank lists that for each operation and the solution.
    first= []
    second = []


    
    solution = []
    
    order(equationList, first, second)

    print(equationList)
    
    solve(equationList, first, second, solution)
    print(first)
    print(second)
    print()
    print(solution)


## Function that marks the location of each arithmetic operator in seperate lists
def order(equation, first, second):
    for i, e in enumerate(equation):
        if e == "*" or e == "/":
            first.append(i)

    for i, e in enumerate(equation):
        if e == "+" or e == "-":
            second.append(i)


#def solve(eq, pos1, pos2, sol):
#    for i, e in enumerate(pos1):
#       if eq[e] == "*":
#            sol.append(float(eq[e-1]) * float(eq[e+1]))
#            
#           eq[e-1] = "TEMP"
#          eq[e] = "TEMP"
#         eq[e+1] = "TEMP"
#        elif eq[e] == "/":
#            sol.append(float(eq[e-1]) / float(eq[e+1]))
#            
#            eq[e-1] ="TEMP"
#            eq[e] = "TEMP"
#            eq[e+1] = "TEMP"

def solve(eq,first, second, sol):
    while "*" in eq or "/" in eq:
        for i, e in enumerate(eq):
            if e == "*":
                eq[i] = float(eq[i-1]) * float(eq[i+1])
                del eq[i+1],eq[i-1]
            elif e == "/":
                eq[i] = float(eq[i-1]) / float(eq[i+1])
                del eq[i+1],eq[i-1]
    print(eq)
            
        























main()


