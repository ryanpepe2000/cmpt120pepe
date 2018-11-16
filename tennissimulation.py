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
        stats.printStats()

def main():
    ts = TennisSimulation(.6,.5,50)
    ts.run()

main()
    
