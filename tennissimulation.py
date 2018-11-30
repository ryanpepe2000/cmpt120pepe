# tennissimulation.py

from simstats import *
from tennismatch import *

class TennisSimulation:
    def __init__(self, probA, probB, n):
        self.probA = probA
        self.probB = probB
        self.n = n

    def run(self):
        stats = SimStats()
        for i in range(self.n):
            match = TennisMatch(self.probA, self.probB)
            match.play()
            stats.update(match)
        stats.printReport()

def main():
    p1 = float(input("Enter the probability that tennis player A will win a game: "))
    p2 = float(input("Enter the probability that tennis player B will win a game: "))
    games = int(input("Enter the number of games to be simulated: "))
    ts = TennisSimulation(p1,p2,games)
    ts.run()

main()
    
