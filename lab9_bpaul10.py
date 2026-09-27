"""
lab9_bpaul10.py
Bernard Paul
The purpose of this program is to be the main driver for a coin toss game. 
The player tosses a coin and compare results and gets coins based off if the results match.
9/27/26

"""

from player import Player

def main():
    #runs the main game
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play_again = "y"

    while play_again.lower() == "y":
        play_again = input("Do you want to toss the coins? (y/n): ")

        if play_again.lower() != "y":
            break
        
        #putting tossing here instead of in toss_coin since its only printed once
        print("Tossing")
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()


        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        #setting win conditions
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()

            print(f"...It's a Match! Player 1 wins a coin.")
        else:
            player1.lose_coin()
            player2.win_coin()
            

            print("...No Match. No one wins a coin.")

        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    #ending the game
    print("--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}.")
    print(f"{player2.get_name()}: {player2.get_wallet()}.")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()