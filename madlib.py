# madlibs.py
# Program that creates a fictional "MadLib" story
# based on user input

def main():
    noun = str(input("Please enter a noun: "))
    animal = str(input("Please enter a type of animal: "))
    verb = str(input("Please enter a verb: "))
    verb2 = str(input("Please enter another verb: "))
    adj = str(input("Please enter adjective: "))
    adj2 = str(input("Please enter another adjective: "))
    place = str(input("Please enter a place: "))

    print("There was once a", noun, "who didn't have many friends. Everyone")
    print("thought that the", noun, "was too", adj + ". The", noun, "liked to", verb)
    print("and", verb2 + ", but everyone thought it was weird. One day the", noun)
    print("went to the", place, "and met a", animal + ". The", animal, "befriended")
    print("the", noun, "and they both lived happily ever after.")
main()
    
        
