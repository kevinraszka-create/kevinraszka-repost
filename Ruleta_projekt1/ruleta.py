import random
import numpy as np 

#   Python Ruleta      
class roulette:
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

    def __init__(self, betType=None, rouletteStyle=None, bankAccount=None, rollNumber=None, rollHistory=None, colorHistory=None):
        #   Set the defualts
        if betType is None:
            self.betType = 'Straight'
        else:
            self.betType = betType
        if rouletteStyle is None:
            self.rouletteStyle = 'American'
        else:
            self.rouletteStyle = rouletteStyle
        if bankAccount is None:
            self.bankAccount = 10000.0
        else:
            self.bankAccount = float(bankAccount)
        if rollNumber is None:
            self.rollNumber = 0
        else:
            self.rollNumber = int(rollNumber)
        if rollHistory is None:
            self.rollHistory = []
        else:
            self.rollHistory = rollHistory    
        if colorHistory is None:
            self.colorHistory = []
        else:
            self.colorHistory = colorHistory
            
    def recordColorHistory(self, theRoll):
        #   was the roll red?
        if theRoll in self.red:
            self.colorHistory.append('Red')
        #   was the roll black?
        elif theRoll in self.black:
            self.colorHistory.append('Black')
        #   if the roll wasn't black or red, then it was green
        else:
            self.colorHistory.append('Green')