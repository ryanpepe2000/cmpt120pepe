# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Ryan Pepe
# Created: 2018-09-25



def main():

    # get user's first and last names
    nameList = name()
    
    # TODO modify this to generate a Marist-style username
    uname = nameList[0] + "." + nameList[1]

    # ask user to create a new password
    passwd = input("Create a new password: ")

    # TODO modify this to ensure the password has at least 8 characters
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one…")
    print("Account configured. Your new email address is",
        uname + "@marist.edu")

def name():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first,last]


main()
