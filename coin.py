"""
Programs name
Bernard Paul
The purpose of this program is to be a class of a single coin.
This coin is tossable and it only knows the state of itself 
either being heads or tails
9/25/26

"""
import random

#coin class represents the coin
class Coin:
    #initializing coin being faced up
    def __init__(self):
        self.sideup = "Heads"

    #randomly tosses the coin 
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    #tells which side is currently up might combine with toss func
    def get_sideup(self):
        return self.sideup