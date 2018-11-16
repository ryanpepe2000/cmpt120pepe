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
    ts = TennisSimulation(.9,.2,50)
    ts.run()

main()
    
