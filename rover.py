# rover.py
# Program to calculate the amount of time for a photo to reach
# Earth from Mars

def main():
    speedLight = 186000
    distance = 34000000

    time = distance / speedLight
    print("The amount of time it takes a photo to travel from Mars to Earth is", time, "seconds")
main()
