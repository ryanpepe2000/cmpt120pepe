# keypad.py
# This program builds a graphical calculator display.

from graphics import *
import calculator


# Creats rectangles with labels and returns those values.
def createButton(values):
    p1 = Point(values[0], values[1])
    p2 = Point(values[0]+ 1, values[1] + 1)
    button = Rectangle(p1,p2)
    button.setFill(values[3])
    label = Text(Point(values[0] + 0.5, values[1] + 0.5), values[2])
    return button, label

# Creates key on keypad for each item in list
def createKeypad(lst):
    keys = []
    for key in lst:
        button, label = createButton(key)
        keys.append([button, label])
    return keys

# Creates a rectangle for screen and returns coordinates and screen text.
def createScreen(screenText):
    
    p1 = Point(0,5)
    p2 = Point(4,6)
    screen = Rectangle(p1,p2)
    screen.setFill("paleTurquoise")
    screenText = Text(Point(2,5.5),screenText)
    return screen, screenText

# Draws all objects
def renderObjects(keys, win, screen, screenText):
    for key in keys:
        key[0].draw(win)
        key[1].draw(win)
    screen.draw(win)
    screenText.draw(win)

# Stores the string of label for each button pressed.
def click(win, keys):
    mouse = win.getMouse()
    
    for e, key in enumerate(keys):
        button, label = createButton(key)

        if button.p1.x < mouse.x < button.p2.x and button.p1.y < mouse.y < button.p2.y:
            return(keys[e][2])

# Creates a value for each button pressed in calculator.
# Numbers/decimals are stored as one item in list.
# Arithmetic operators are stored as one value
# "Del" and "+/-" are stored as one.
# "=" calculates function

def createNumber(win,num,numList,keyList,mouse, screenText):

    # NUMBERS
    if mouse != "*" and mouse != "/" and mouse != "+" and mouse != "-" and mouse != "=" and mouse != "+/-" and mouse != "Del":
        if mouse != ".":
            num.append(str(mouse))
        elif mouse == ".":
            num.append(".")
        print(num)
        screenText.setText(num)
       
    # ARITHMETIC OPERATORS  
    elif mouse == "*" or mouse == "/" or mouse == "+" or mouse == "-":
        try:
            if float(numList[-1]) > 0:
                numList.append("".join(num))
                if mouse == "*" or mouse == "/" or mouse == "+" or mouse == "-":
                    numList.append(mouse)
                print(numList)
                num.clear()
        except:
            numList.append("".join(num))
            if mouse == "*" or mouse == "/" or mouse == "+" or mouse == "-":
                numList.append(mouse)
            print(numList)
            num.clear()
        else:
            if mouse == "*" or mouse == "/" or mouse == "+" or mouse == "-":
                numList.append(mouse)
            print(numList)
            num.clear()

    # NEGATIVE BUTTON
    elif mouse == "+/-":
        numList.append("".join(num))
        numList[-1] = str(float(numList[-1]) * -1)

        print(numList)

    # DELETE BUTTON
    elif mouse == "Del":
        numList.clear() 
        num.clear()
        screenText.setText("")

    # CALCULATE BUTTON
    elif mouse == "=":
        try:
            if float(numList[-1]) > 0:
                numList.append("".join(num))
                print(numList)
                print(solution)
        except:
            numList.append("".join(num))
            print(numList)

        
# Sets text in screen to the list of values.
def display(win,i,num,numList,screenText):
    print(i)
    if i % 2 == 0:
        screenText.setText(" ".join(numList))
        return i + 1
    else:
        screenText.setText("".join(num))
        return i
# Loops creation of numbers in list and display of them. 
def loopCalc(win,screen,numList,keyList,screenText):
    num = []
    i = 1
    while True:

            mouse = click(win,keyList)
            createNumber(win,num,numList,keyList,mouse,screenText)

            isplayScreen = display(win,i, num, numList,screenText)
            

            # Calls to calculate.py to compute solution
            if mouse == "=":
                solution = calculator.main(numList)
                screenText.setText(solution)

            # QUIT BUTTON
            if mouse == "Quit":
                win.close()
                pass

def main():
    numberList = []
    #List containing coordinates, values, and colors for each button.
    keyList = [[0,0,"+/-","orange"],     [1,0,"0","navajoWhite"], [2,0,".","orange"],        [3,0,"=","orange"],
              [0,1,"1","navajoWhite"],   [1,1,"2","navajoWhite"], [2,1,"3","navajoWhite"],   [3,1,"+","orange"],
              [0,2,"4","navajoWhite"],   [1,2,"5","navajoWhite"], [2,2,"6","navajoWhite"],   [3,2,"-","orange"],
              [0,3,"7","navajoWhite"],   [1,3,"8","navajoWhite"], [2,3,"9","navajoWhite"],   [3,3,"*","orange"],
              [0,4,"Quit","white"],          [1,4,"","white"],        [2,4,"Del","orange"],      [3,4,"/","orange"]]

    keys = createKeypad(keyList)
    screen, screenText = createScreen(numberList)

    win = GraphWin("Key Pad",300,400)
    win.setCoords(0.0, 0.0, 4.0, 6.0)
    
    renderObjects(keys, win, screen, screenText)
    loopCalc(win,screen,numberList,keyList,screenText)
    
main()
