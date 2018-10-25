# keypad.py
# This program builds a graphical calculator display.

from graphics import *


def createButton(values):
    p1 = Point(values[0], values[1])
    p2 = Point(values[0]+ 1, values[1] + 1)
    button = Rectangle(p1,p2)
    button.setFill(values[3])
    label = Text(Point(values[0] + 0.5, values[1] + 0.5), values[2])
    return button, label

def createKeypad(lst):
    keys = []
    for key in lst:
        button, label = createButton(key)
        keys.append([button, label])
    return keys

def createScreen(screenText):
    
    p1 = Point(0,5)
    p2 = Point(4,6)
    screen = Rectangle(p1,p2)
    screen.setFill("paleTurquoise")
    screenText = Text(Point(2,5.5),screenText)
    return screen, screenText

def renderObjects(keys, win, screen, screenText):
    for key in keys:
        key[0].draw(win)
        key[1].draw(win)
    screen.draw(win)
    screenText.draw(win)

def click(win, keys):
    mouse = win.getMouse()
    
    for e, key in enumerate(keys):
        button, label = createButton(key)

        if button.p1.x < mouse.x < button.p2.x and button.p1.y < mouse.y < button.p2.y:
            return(keys[e][2])

def createNumber(win,num,numList,keyList,mouse, screenText):
    if mouse != "*" and mouse != "/" and mouse != "+" and mouse != "-" and mouse != "=" and mouse != "+/-":
        if mouse != ".":
            num.append(str(mouse))
        elif mouse == ".":
            num.append(".")
        print(num)
        screenText = num
        
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
        
    elif mouse == "+/-":
        numList.append("".join(num))
        numList[-1] = str(float(numList[-1]) * -1)

        print(numList)
     
    
    elif mouse == "=":
        numList.append("".join(num))
        print(numList)


def createList(win,numList,keyList,screenText):
    num = []
    while True:

            mouse = click(win,keyList)
            createNumber(win,num,numList,keyList,mouse,screenText)
            print(numList)

def main():
    numberList = []
    keyList = [[0,0,"+/-","orange"],     [1,0,"0","navajoWhite"], [2,0,".","orange"],        [3,0,"=","orange"],
              [0,1,"1","navajoWhite"],   [1,1,"2","navajoWhite"], [2,1,"3","navajoWhite"],   [3,1,"+","orange"],
              [0,2,"4","navajoWhite"],   [1,2,"5","navajoWhite"], [2,2,"6","navajoWhite"],   [3,2,"-","orange"],
              [0,3,"7","navajoWhite"],   [1,3,"8","navajoWhite"], [2,3,"9","navajoWhite"],   [3,3,"*","orange"],
              [0,4,"","white"],          [1,4,"","white"],        [2,4,"Del","orange"],      [3,4,"/","orange"]]

    keys = createKeypad(keyList)
    screen, screenText = createScreen(numberList)

    win = GraphWin("Key Pad",300,400)
    win.setCoords(0.0, 0.0, 4.0, 6.0)
    
    renderObjects(keys, win, screen, screenText)
    createList(win,numberList,keyList,screenText)
main()