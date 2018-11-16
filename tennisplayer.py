# tennisplayer.py
from random import *

class TennisPlayer:
    def __init__(self, prob):
        self.prob = prob
        self.setScore = 0
        self.score = 0

    def incSetScore(self):
        self.setScore = self.setScore + 1

    def incScore(self):
        if self.score == 0:
            self.score = 15
        elif self.score == 15:
            self.score = 30
        elif self.score == 30:
            self.score = 40
        else:
            self.score = self.score + 1

    def getSetScore(self):
        return self.setScore

    def getScore(self):
        return self.score

    def resetScore(self):
        self.score = 0

    def winsPoint(self):
        if random() < self.prob:
            return True
        else:
            return False
        
