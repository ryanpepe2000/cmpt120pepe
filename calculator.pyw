# calculator.pyw
# This program builds a graphical calculator keypad
from graphics import *
from calculator_functions import *
from button import *
import sys


class Display:
    """Class for elements of calculator display"""
    def __init__(self):
        pass
class Calculator:
    """ Encloses all the functionality of the calculator"""
    def __init__(self):
        pass
        
# Creates buttons based on the coordinates in keyList array
def createButton(values):
    p1 = Point(values[0] + .025, values[1] + .025)
    p2 = Point(values[0] + .99, values[1] + .99)
    button = Rectangle(p1, p2)
    button.setFill(values[3])
    button.setOutline(values[3])
    label = Text(Point(values[0] + .5, values[1] + .5), values[2])
    return button, label

# Traverses list and makes an array of button objects and text objects.
def createKeypad(lst):
    keys = []
    for key in lst:
        button, label = createButton(key)
        keys.append([button, label])
    return keys

# Draws each individual key
def renderKeys(keys, win):
    for key in keys:
        key[0].draw(win)
        key[1].draw(win)

# Returns the value of the button to append to the equation
def getButton(click, keyList):
    x = click.getX()
    y = click.getY()

    for i in range(len(keyList)):
        if keyList[i][1] == int(y): # floor
            for j in range(i,len(keyList)):
                if keyList[j][0] == int(x):
                    if keyList[j][2] in ['*','/','+','-']:
                        return " " + keyList[j][2] + " "
                    else:
                        return keyList[j][2]
                    
# Creates a graphical window, display box, and text to represent output
def createDisplay(keyList):
    keys = createKeypad(keyList)

    win = GraphWin("Key Pad", 300,400)
    win.setCoords(0.0, 0.0, 4.0, 7.0)
    win.setBackground("navy")
    display = Rectangle(Point(0.025,6.95),Point(3.975,6.05))
    display.setFill("white")
    display.draw(win)
    text = Text(Point(2,6.5), "")
    text.draw(win)
    memText = Text(Point(3.3,6.2),"")
    memText.setSize(10)
    memText.draw(win)
                   

    renderKeys(keys, win)
    return win, display, text, memText

def main():

    # An array of coordinates, key value, and button color.
    keyList = [[0,0,"+/-","orange"],     [1,0,"0","navajoWhite"], [2,0,".","orange"],        [3,0,"=","orange"],
              [0,1,"1","navajoWhite"],   [1,1,"2","navajoWhite"], [2,1,"3","navajoWhite"],   [3,1,"+","orange"],
              [0,2,"4","navajoWhite"],   [1,2,"5","navajoWhite"], [2,2,"6","navajoWhite"],   [3,2,"-","orange"],
              [0,3,"7","navajoWhite"],   [1,3,"8","navajoWhite"], [2,3,"9","navajoWhite"],   [3,3,"*","orange"],
              [0,4,"Quit","orange"],     [1,4,"C","orange"],      [2,4,"CE","orange"],       [3,4,"/","orange"],
              [0,5,"M+","silver"],       [1,5,"M-","silver"],     [2,5,"MR","silver"],       [3,5,"MC","silver"]]

    win, display, text, memText = createDisplay(keyList)

    equation = ""
    memory = 0.0
    
    while True:
        click = win.getMouse()
        buttonText = getButton(click,keyList)
        print(buttonText)

        # If an error is returned, clicking will reset calculator.
        if equation == "Error":
            equation = ""
            
        # Attempts to performs calculator functions.
        try:
            # Solves the equation in calculator
            if buttonText == "=": 
                result = solve(equation.split())
                equation = str(result)

            # Multiplies last digit in equation by -1 and replaces existing last digit
            elif buttonText == "+/-":
                lastDigit = float(equation.split()[-1])
                lastDigit = lastDigit * -1
                equation = " ".join(equation.split()[:-1]) + " " + str(lastDigit)
                
            # Clears the entire calculator
            elif buttonText == "C":
                result = ""
                equation = str(result)

            # Clears a single entry from calculator
            elif buttonText == "CE":
                equation = " ".join(equation.split()[:-1]) + " "
                result = equation

            # Quits the calculator
            elif buttonText == "Quit":
                break


            # Handles the four memory buttons (add, subtract, recall, clear)

            #############################################################

            elif buttonText == "M+":
                memory = memory + float(solve(equation.split()))
                memText.setText("mem: " + str(memory))
            elif buttonText == "M-":
                memory = memory - float(solve(equation.split()))
                memText.setText("mem: " + str(memory))
            elif buttonText == "MR":
                equation = equation + str(memory)
                memText.setText("mem: " + str(memory))
            elif buttonText == "MC":
                memory = 0.0
                memText.setText("mem: " + str(memory))
                
            ##############################################################
                
            # Concatenates equation string with whatever number is clicked.
            else:
                equation = equation + buttonText
                
        # If any errors are found (divide by zero), will display "error"
        except:
            equation = "Error"
            
        # After EACH button is pressed, the display's text is altered    
        text.setText(equation)
        print(equation)
    win.close()
    sys.exit()
    
main()


    
           
