# personality.py
# Ryan Pepe
# CMPT120
# 30 October 2018

import random

states = ["anger", "disgust", "fear", "happiness", "saddness", "surprise"]
actions = ["reward", "punish", "threaten", "joke"]
transitions =  [[0,0,1],[0,1,4],[0,2,2],[0,3,0],
                [1,0,3],[1,1,5],[1,2,2],[1,3,0],
                [2,0,3],[2,1,5],[2,2,2],[2,3,3],
                [3,0,3],[3,1,4],[2,2,2],[3,3,3],
                [4,0,3],[4,1,0],[4,2,2],[4,3,3],
                [5,0,3],[5,1,0],[5,2,5],[5,3,3]]
            

# returns integer of index of actions
def getInteraction(): 
    userAction = input("What would you like to do? (reward, punish, threaten, joke): ")
    for interaction in actions:
        if interaction == userAction.lower():
            return int(actions.index(interaction))

def lookupEmotion(currEmotion, userAction): # return integer corresponding to emotion
    
    for i, e in enumerate(transitions):
        if e[0] == currEmotion:
            for j in range(i,i+3):
                if e[1] == userAction:
                    return(e[2])



def main():
    currEmotion = int(random.random() * 6)
    print("I am currently experiencing", states[currEmotion] + "!")
    while True:
        userAction = getInteraction()
        
        emotion = states[lookupEmotion(currEmotion, userAction)]

        if emotion == "anger":
            print("I AM ANGRY!")
        elif emotion == "disgust":
            print("Wow. I am disgusted with you.")
        elif emotion == "fear":
            print("Please stop, you are scaring me.")
        elif emotion == "happiness":
            print("I am so happy.")
        elif emotion == "saddness":
            print("I think I am going to cry.")
        elif emotion == "surprise":
            print("I am so surprised!")

main()
