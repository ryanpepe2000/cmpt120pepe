# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Ryan Pepe
# Created: 2018-09-25



def main():

    # Assigns first and last name input to the list 'nameList'
    nameList = name()
    
    # Assigns mastistUName function to the 'uname' variable.
    uname = maristUName(nameList[0],nameList[1])

    sPassword = createPassword()
    checkPassword(sPassword)
    
    print("The force is strong in this one…")
    print("Account configured. Your new email address is",
        uname + "@marist.edu")

# Creates function that returns a list from user's first and last name.
def name():
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()
    return [first,last]

# Creates function that returns user's first and last name seperated
# by '.' as a string.
def maristUName(first,last):
    return first + "." + last

# Creates a function that allows user input to be stored as a password.
def createPassword():
    passwd = input("Create a new password: ")
    return passwd


# Creates a function that checks a password's strength.
def checkPassword(passwd):
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    return passwd


    


main()
