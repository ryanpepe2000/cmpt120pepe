# guessing-game.py
# Ryan Pepe
# CMPT 120
# 10/2/2018

def main():
    name = ""
    while True:
        print("Thinking of an animal...\n")
        name = str(input("Guess the type of animal: ")).lower()
        if name == "pig":
            print("\nCongratulations, you guessed correctly!\n")
            likeAnimal = str(input("Do you like this animal?: "))
            if likeAnimal[0].lower() == "y":
                print("\nThat's awesome, me too!")
            elif likeAnimal[0].lower() == "n":
                print("\nWhy not!? Pigs are the best!")
            break
        elif name[0].lower() == "q":
            break
        else:
            print("\nSorry, you guessed wrong. Try again!\n")
main()
            
    
                   
