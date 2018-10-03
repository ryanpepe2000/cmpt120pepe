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
    print()
    print("Solution: ", expressionList[0])

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

#Class Project Tips

# range(1, len(list), 2)
# Looks at all operators
#
# while len((list) > 1

#for i in range(1,len(list),2)
# if list[i] == "*"
#   result = float(list[i-1]) * float(list[i+1])
#    del list[i-1:i+1]
#   list.insert(i-1, result)
#   break
# elif list[i] == "/"
