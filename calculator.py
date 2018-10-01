# calculator.py
# CMPT 120
# Date Created: 2018-09-28
# Author: Ryan Pepe

def main():
    equation = str(input("Enter an equation with any basic arithmetic operator: "))

    # Turns user's input into a list of each number and arithmetic operator, regardless
    # of whether the user inputted spaces in between operators.
    equationList = equation.replace("+", " + ").replace("*"," * ").replace("/"," / ").split()
    print(equationList)
    # First computes multiplication/division, then computes addition/subtraction.
    multDiv(equationList)
    addSub(equationList)

    # Displays solution
    print()
    print("Solution: ", equationList[0])
# Function that computes multiplication/division.          
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
# Function that computes addition/subtraction.          
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


