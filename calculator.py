# calculator.py
# CMPT 120
# Date Created: 2018-09-28
# Author: Ryan Pepe


def main():
    expression = str(input("Enter an expression with any basic arithmetic operator: "))

    # Turns user's input into a list of each number and arithmetic operator, regardless
    # of whether the user inputted spaces in between operators.
    expressionList = expression.replace("+", " + ").replace("*"," * ").replace("/"," / ").split()

    # First computes multiplication/division, then computes addition/subtraction.
    multDiv(expressionList)
    addSub(expressionList)

    # Displays solution
    print("\nSolution: ", expressionList[0])

# Function that computes multiplication/division.          
def multDiv(ex):
    while "*" in ex or "/" in ex:
        for i, e in enumerate(ex):
            if e == "*":
                ex[i] = float(ex[i-1]) * float(ex[i+1])
                del ex[i+1],ex[i-1]
                break
            elif e == "/":
                ex[i] = float(ex[i-1]) / float(ex[i+1])
                del ex[i+1],ex[i-1]
                break

# Function that computes addition/subtraction.          
def addSub(ex):
    while "+" in ex or "-" in ex:
        for i, e in enumerate(ex):
            if e == "+":
                ex[i] = float(ex[i+1]) + float(ex[i-1])
                del ex[i+1],ex[i-1]
                break
            elif e == "-":
                ex[i] = float(ex[i-1]) - float(ex[i+1])
                del ex[i+1],ex[i-1]
                break
    
main()
