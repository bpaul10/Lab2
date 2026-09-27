"""
Programs name
Bernard Paul
The purpose of this program is to be the class of the player
the player will have a name a wallet qith gcoins and the coin 
object to toss

9/27/26

"""

from coin import Coin

class Player:
    #Class is the player in a maching coin game

    def __init__(self, name, ):
        #initialize the player with a name, wallet of 20 coins, and a coin object
        self.name = name
        self.wallet = 20
        self.coin = Coin()
        
    def toss_coin(self):
        #players coin toss
        self.coin.toss()

    def get_coin_side(self):
        #gets the side of the coin
        return self.coin.get_sideup()

    def win_coin(self):
        #player wins a coin
        self.wallet += 1

    def lose_coin(self):
        #player loses a coin
        self.wallet -= 1

    def get_wallet(self):
        #gets the players wallet amount
        return self.wallet

    def get_name(self):
        #gets the players name
        return self.name    