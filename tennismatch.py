# tennismatch.py
from random import random
from tennisplayer import *
# class to simulate a tennis match
class TennisMatch:
    def __init__(self, probA, probB):
        self.playerA = TennisPlayer(probA)
        self.playerB = TennisPlayer(probB)

    def play(self):
        serving = self.playerA
        for i in range(3):
            tSet = TennisSet(self.playerA, self.playerB, serving)
            player = tSet.play()
            player.incSetScore()
            serving = self.switchServer(serving)

    def switchServer(self, serving):
        if serving == self.playerA:
            serving = self.playerB
        else:
            serving = self.playerA
        return serving

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()

# class to simulate a tennis set  
class TennisSet:
    def __init__(self, playerA, playerB, serving):
        self.playerA = playerA
        self.playerB = playerB
        self.serving = serving

    def play(self):
        while not self.__isOver():
            game = Game(self.playerA, self.playerB, self.serving)
            player = game.play()
            player.incSetScore()
                
        if self.playerA.getSetScore() > self.playerB.getSetScore():
            return self.playerA
        else:
            return self.playerB

    def __isOver(self):
        return (self.playerA.getSetScore() >= 6 or self.playerB.getSetScore() >= 6) \
            and abs(self.playerA.getSetScore() - self.playerB.getSetScore()) >= 2

# class to simulate a tennis game
class Game:
    def __init__(self, playerA, playerB, serving):
        self.playerA = playerA
        self.playerB = playerB
        self.serving = serving
        self.playerA.resetScore()
        self.playerB.resetScore()

    def play(self):
        while not self.__isOver():
            if self.serving.winsPoint():
                self.serving.incScore()
            elif self.serving == self.playerA:
                self.playerB.incScore()
            else:
                self.playerA.incScore()
        if self.playerA.getScore() > self.playerB.getScore():
            return self.playerA
        else:
            return self.playerB

    def __isOver(self):
        if self.playerA.getScore() > 40 and self.playerB.getScore() < 40:
            return True
        elif self.playerA.getScore() < 40 and self.playerB.getScore() > 40:
            return True
        elif self.playerA.getScore() >= 40 and self.playerB.getScore() >= 40 \
             and abs(self.playerA.getScore() - self.playerB.getScore()) >= 2:
            return True
        else:
            return False

    
