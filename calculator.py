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
                break
            elif e == "/":
                eq[i] = float(eq[i-1]) / float(eq[i+1])
                del eq[i+1],eq[i-1]
                break
    print(eq)
    
# Function that computes addition/subtraction.          
def addSub(eq):
    while "+" in eq or "-" in eq:
        for i, e in enumerate(eq):
            if e == "+":
                eq[i] = float(eq[i+1]) + float(eq[i-1])
                del eq[i+1],eq[i-1]
                break
            elif e == "-":
                eq[i] = float(eq[i-1]) - float(eq[i+1])
                del eq[i+1],eq[i-1]
                break
               
    print(eq)
    
main()

#### 8 / 2 + 4 * 4 - 3 + 2 * 2 / 6 DOES NOT WORK == 16.3333333333
## TRULY EQUALS 17.6666666666666666666

#Class PRoject notes
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
