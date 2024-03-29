# calculatorapp.pyw
from graphics import *
from button import *
from math import *

class CalculatorApp:
    """ Encloses all the functionality of the calculator (display and buttons are subclass)"""
    def __init__(self):
        self.win = GraphWin("Calculator", 300, 400)
        self.win.setCoords(0.0, 0.0, 4.0, 9.0)
        self.win.setBackground("navy")
        self.display = Display(self.win)
        self.keypad = Keypad(self.win)
        self.calcEngine = CalculatorEngine(self.win)

    def run(self):
        while True:
            click = self.win.getMouse()
            # Get the key that was pressed
            key = self.keypad.getKey(click)
            print(key)
            # Process the key and get the result
            result = self.calcEngine.process(key)
            # Display the result
            self.display.update(result)
            
class Display:
    def __init__(self,win):
        self.rect = Rectangle(Point(0.025,8.95), Point(3.975,8.05))
        self.rect.setFill("white")
        self.rect.draw(win)
        self.text = Text(Point(2,8.5),"")
        self.text.draw(win)

    def update(self, result):
        # Updates the display with the current result
        self.text.setText(result)

class Keypad:
    def __init__(self, win):
        self.win = win
        # Creates a list of each button as objects
        self.buttons = [
            Button(win, Point(.5,.5), 1, 1, "+/-", "orange", 12), 
            Button(win, Point(1.5,.5), 1, 1, "0", "navajoWhite", 12),
            Button(win, Point(2.5,.5), 1, 1, "•", "orange", 12),
            Button(win, Point(3.5,.5), 1, 1, "=", "orange", 12),
            Button(win, Point(.5,1.5), 1, 1, "1", "navajoWhite", 12),
            Button(win, Point(1.5,1.5), 1, 1, "2", "navajoWhite", 12),
            Button(win, Point(2.5,1.5), 1, 1, "3", "navajoWhite", 12),
            Button(win, Point(3.5,1.5), 1, 1, "+", "orange", 12),
            Button(win, Point(.5,2.5), 1, 1, "4", "navajoWhite", 12),
            Button(win, Point(1.5,2.5), 1, 1, "5", "navajoWhite", 12),
            Button(win, Point(2.5,2.5), 1, 1, "6", "navajoWhite", 12),
            Button(win, Point(3.5,2.5), 1, 1, "-", "orange", 12),
            Button(win, Point(.5,3.5), 1, 1, "7", "navajoWhite", 12),
            Button(win, Point(1.5,3.5), 1, 1, "8", "navajoWhite", 12),
            Button(win, Point(2.5,3.5), 1, 1, "9", "navajoWhite", 12),
            Button(win, Point(3.5,3.5), 1, 1, "*", "orange", 12),
            Button(win, Point(.5,4.5), 1, 1, "(", "orange", 12),
            Button(win, Point(1.5,4.5), 1, 1, ")", "orange", 12),
            Button(win, Point(2.5,4.5), 1, 1, "x²", "orange", 12),
            Button(win, Point(3.5,4.5), 1, 1, "/", "orange", 12),
            Button(win, Point(.5,5.25), 1, .5, "sin", "orange", 12),
            Button(win, Point(1.5,5.25), 1, .5, "cos", "orange", 12),
            Button(win, Point(2.5,5.25), 1, .5, "tan", "orange", 12),
            Button(win, Point(3.5,5.5), 1, 1, "1 / x", "orange", 12),
            Button(win, Point(.5,5.75), 1, .5, "asin", "orange", 12),
            Button(win, Point(1.5,5.75), 1, .5, "acos", "orange", 12),
            Button(win, Point(2.5,5.75), 1, .5, "atan", "orange", 12),
            Button(win, Point(.5,6.5), 1, 1, "Quit", "dimgrey", 12),
            Button(win, Point(1.5,6.5), 1, 1, "C", "dimgrey", 12),
            Button(win, Point(2.5,6.5), 1, 1, "Del", "dimgrey", 12),
            Button(win, Point(3.5,6.5), 1, 1, "ln(x)", "orange", 12),
            Button(win, Point(.5,7.5), 1, 1, "M+", "silver", 12),
            Button(win, Point(1.5,7.5), 1, 1, "M-", "silver", 12),
            Button(win, Point(2.5,7.5), 1, 1, "MR", "silver", 12),
            Button(win, Point(3.5,7.5), 1, 1, "MC", "silver", 12)
            ]
        
        

    def getKey(self, p):
        for button in self.buttons:
            if button.clicked(p):     
                return button.getLabel()

class CalculatorEngine:
    def __init__(self,win):
        self.equation = ""
        self.win = win
        self.number = []
        self.memory = 0.0

    def process(self, key):
        # Processes input and returns the current equation
        try:
            if key in ["0","1","2","3","4","5","6","7","8","9"]:
                self.equation = self.equation + key
                return self.equation
            elif key == "•":
                self.equation = self.equation + "."
                return self.equation
            elif key in ["*", "/", "+", "-"]:
                self.equation = self.equation + " " + key + " "
                return self.equation
            elif key == "(":
                self.equation = self.equation + key + " "
                return self.equation
            elif key == ")":
                self.equation = self.equation + " " + key
                return self.equation
            elif key == "+/-":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = lastDigit * -1
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "C":
                result = ""
                self.equation = str(result)
                return self.equation
            elif key == "Del":
                self.equation = " ".join(self.equation.split()[:-1]) + " "
                return self.equation
            elif key == "Quit":
                self.win.close()
            elif key == "sin":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = sin(lastDigit)
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "cos":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = cos(lastDigit)
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "tan":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = tan(lastDigit)
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "asin":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = asin(lastDigit)
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "acos":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = acos(lastDigit)
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "atan":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = atan(lastDigit)
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "1 / x":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = 1 / lastDigit
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "x²":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = lastDigit ** 2
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "ln(x)":
                lastDigit = float(self.equation.split()[-1])
                lastDigit = log(lastDigit)
                self.equation = " ".join(self.equation.split()[:-1]) + " " + str(lastDigit)
                return self.equation
            elif key == "M+":
                self.memory = self.memory + float(self.equation)
                print("Mem: ", self.memory)
            elif key == "M-":
                self.memory = self.memory - float((self.equation))
                print("Mem: " , self.memory)
            elif key == "MR":
                self.equation = self.equation + str(self.memory)
                return self.equation
            elif key == "MC":
                self.memory = 0.0
            elif key == "=":
                self.equation = self.equation.split()  
                self.equation = ["("] + self.equation               # Adds parentheses to 
                self.equation.append(")")                           # enclose expression
                self.equation = str(self.__answer(self.equation))
                return self.equation
    
        except:
            self.equation = ""
            return "Error"

    def __solve(self, equation):
        # Internal Function to solve equation
        while "*" in equation or "/" in equation:
            if type(equation) == str:
                equation = equation.split()
            for i, e in enumerate(equation):
                if e == "*":
                    equation[i] = float(equation[i-1]) * float(equation[i+1])
                    del equation[i+1],equation[i-1]
                    break
                elif e == "/":
                    equation[i] = float(equation[i-1]) / float(equation[i+1])
                    del equation[i+1],equation[i-1]
                    break
        while "+" in equation or "-" in equation:
            if type(equation) == str:
                equation = equation.split()
            for i, e in enumerate(equation):
                if e == "+":
                    equation[i] = float(equation[i+1]) + float(equation[i-1])
                    del equation[i+1],equation[i-1]
                    break
                elif e == "-":
                    equation[i] = float(equation[i-1]) - float(equation[i+1])
                    del equation[i+1],equation[i-1]
                    break
        
        return equation[0]

    #
    #  RECURSIVE PARENTHESES FUNCTION
    #
    def __parenthesis(self, ex):
        if not "(" in ex and not ")" in ex:
            return ex
        first = ex.index("(")
        last = len(ex) - 1 - ex[::-1].index(")")
        return self.__parenthesis(ex[first+1:last])

    # While parentheses are still in list, continue recursively solving inner parentheses
    def __answer(self, ex):
        while "(" in ex or ")" in ex:
            first = "".join(ex).rindex("(")
            last = ex.index(")")
            innerParen = str(self.__solve(self.__parenthesis(ex)))
            ex[first] = innerParen
            del ex[first+1:last+1]
        return ex[0]  

def main():
    calc = CalculatorApp()
    calc.run()

main()
