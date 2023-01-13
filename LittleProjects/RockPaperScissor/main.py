from random import randint
from time import sleep
from art import Art


class Game:
    def __init__(self) -> None:
        while True:
            self.gameModes()
            gameMode = int(input("Enter a number: "))
            if gameMode == 1:
                self.playerVSCom()
            elif gameMode == 2:
                self.playerVSplayer()
            elif gameMode == 3:
                self.computerVScomputer()
            else:
                print("The program is being terminated")
                break

    def playerVSCom(self) ->None:
        scoreboard = [0,0] #[0] = player, [1] COM
        while True:
            comDecision = randint(1,3)
            print("SCOREBOARD: PLAYER: {} COMPUTER: {}".format(scoreboard[0],scoreboard[1]))
            self.printChoices()
            playerDecision = int(input("Choose a hand: "))
            outcome = self.gameResult(playerDecision,comDecision)
            if outcome == 1:
                scoreboard[0] +=1
                print("PLAYER +1 POINT")
                if scoreboard[0] == 3:
                    print("THE PLAYER HAS WON")
                    break
            elif outcome == -1:
                scoreboard[1] +=1
                print("COMPUTER +1 POINT")
                if scoreboard[1] == 3:
                    print("THE COMPUTER HAS WON")
                    break
            else:
                print("IT'S A TIE")

    def playerVSplayer(self) -> None:
        scoreboard = [0,0] #[0] player 1, [1] player 2
        while True:
            print("SCOREBOARD: PLAYER ONE: {} PLAYER TWO: {}".format(scoreboard[0],scoreboard[1]))
            self.printChoices()
            player1Decision = int(input("Player 1 choose:"))
            print("SCOREBOARD: PLAYER ONE: {} PLAYER TWO: {}".format(scoreboard[0],scoreboard[1]))
            self.printChoices()
            player2Decision = int(input("Player 2 choose:"))
            outcome = self.gameResult(player1Decision,player2Decision)
            if outcome == 1:
                scoreboard[0] +=1
                print("PLAYER1 +1 POINT")
                if scoreboard[0] ==3:
                    print("PLAYER 1 HAS WON!")
                    break
            elif outcome == -1:
                scoreboard[1] +=1
                print("PLAYER2 +1 POINT")
                if scoreboard[1] == 3:
                    print("PLAYER 2 HAS WON!")
                    break
            else:
                print("IT'S A TIE")

    def computerVScomputer(self) -> None:
        scoreboard = [0,0] #[0] = COM1 [1] = COM2
        while True: 
            com1Decision = randint(1,3)
            com2Decision = randint(1,3)
            print("SCOREBOARD: COMPUTER ONE: {} COMPUTER TWO: {}".format(scoreboard[0],scoreboard[1]))
            if com1Decision == 1:
                print("Computer one choosed: ROCK")
                sleep(1)
            elif com1Decision == 2:
                print("Computer one choosed: PAPER")
                sleep(1)
            elif com1Decision == 3:
                print("Computer one choosed: SCISSOR")
                sleep(1)
            if com2Decision == 1:
                print("Computer two choosed: ROCK")
                sleep(1)
            elif com2Decision == 2:
                print("Computer two choosed: PAPER")
                sleep(1)
            elif com2Decision == 3:
                print("Computer two choosed: SCISSOR")
                sleep(1)
            outcome = self.gameResult(com1Decision,com2Decision)
            if outcome == 1:
                scoreboard[0] +=1
                print("COMPUTER ONE +1 POINT")
                if scoreboard[0] ==3:
                    print("COMPUTER ONE HAS WON!")
                    break
            elif outcome == -1:
                scoreboard[1] +=1
                print("COMPUTER TWO +1 POINT")
                if scoreboard[1] == 3:
                    print("COMPUTER TWO HAS WON!")
                    break
            else:
                print("IT'S A TIE")

    def gameModes(self) -> None:
        print("ROCK PAPER SCISSOR")
        print("Choose the game mode you want:")
        print("1 : Player vs Computer")
        print("2 : Player vs Player")
        print("3 : Computer vs Computer")
        print("4 : Exit")

    def printChoices(self) -> None:
        draw = Art()
        print("1:      2:      3:    ")
        print(draw.rock(), draw.paper(), draw.scissor())

    
    def gameResult(self,player1, player2) -> int:
        """Parameters:\n\nintegers that represents Rock, Paper and Scissor\n\nReturn: \n0: tie\n1: player 1 wins\n2: player 2 wins"""
        if player1 == 1: #Player 1 chooses rock
            if player2 == 1: #TIE
                return 0
            elif player2 == 2:#Player one loses
                return -1
            elif player2 == 3:#Player one wins
                return 1
        elif player1 == 2: #Player 1 chooses paper
            if player2 == 1: #Player one wins 
                return 1
            elif player2 == 2:#TIE
                return 0
            elif player2 == 3:#Player one loses
                return -1
        else:
            if player2 == 1: #Player one loses 
                return -1
            elif player2 == 2:#Player one wins
                return 1
            elif player2 == 3:#TIE
                return 0



if __name__ == "__main__":
    Game()

#Author: Ale Pagan Andujar
#Github: print-Eruki