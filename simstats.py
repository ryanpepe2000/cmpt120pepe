# simstats.py

class SimStats:
   def __init__(self):
       self.winsA = 0
       self.winsB = 0
       self.shutsA = 0
       self.shutsB = 0

   def update(self, game):
        a, b = game.getScores()
        if a > b:
            self.winsA = self.winsA + 1
            if b == 0:
                self.shutsA = self.shutsA + 1
        else:
            self.winsB = self.winsB + 1
            if b == 0:
                self.shutsB = self.shutsB + 1

   def printReport(self):
        # Print a nicely formatted report
        n = self.winsA + self.winsB
        print("Summary of", n ,"games:\n")
        print("          wins (% total)  shutouts (% wins) ")
        print("-------------------------------------------")
        self.printLine("A", self.winsA, self.shutsA, n)
        self.printLine("B", self.winsB, self.shutsB, n)

   def printLine(self, label, wins, shuts, n):
        template = "Player {0}:{1:5}  ({2:5.1%}) {3:11}    ({4})"
        if wins == 0:
            shutStr = "----- "
        else:
            shutStr = "{0:4.1%}".format(float(shuts)/wins)
        print (template.format(label, wins, float(wins)/n,\
            shuts, shutStr))
        
