# CMPT 120 - Lab #6
# Ryan Pepe
# 10/16/2018
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()
        if cmd == "add" or cmd == "sub" or cmd == "mult" or cmd == "div":
            if cmd == "add":
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                result = num1 + num2
            elif cmd == "sub":
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                result = num1 - num2
            elif cmd == "mult":
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                result = num1 * num2
            elif cmd == "div":
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                result = num1 // num2
            print("The result is " + str(result) + ".\n")
        elif cmd == "quit":
            break
        else:
            print("'"+cmd+"'", "is not a valid command.")

def main():
    showIntro()
    doLoop()
    showOutro()
main()
