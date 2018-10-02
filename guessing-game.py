# guessing-game.py
# Ryan Pepe
# CMPT 120
# 10/2/2018

def main():
    name = ""
    while True:
        print("Thinking of an animal...\n")
        name = str(input("Guess the type of animal: "))
        if name == "pig":
            print("\nCongratulations, you guessed correctly!")
            break
        else:
            print("\nSorry, you guessed wrong. Try again!")
main()
            
    
                   
