import enum
import random

from Card import Card
from Move import Move
from Player import Player
from Totem import Totem


class Game:
    def __init__(self):
        self.players = []
        self.deck = []
        self.totems = []
        self.history = []
        self.activePlayer = None

    def init(self, playerNumber=2):
        for i in range(playerNumber):
            self.players.append(Player(i))

        for number in range(1, 10):
            for color in Color:
                self.deck.append(Card(number, color))

        for i in range(9):
            self.totems.append(Totem())

    def setPlayerNames(self, names):
        i = 0
        for player in self.players:
            player.name = names[i]
            i += 1

    def displayBoard(self):
        self.showHands()
        print("\nCurrent player:", self.activePlayer.name)
        i = 0
        for totem in self.totems:
            stackString0 = " ".join(
                ["{:1}:{:6}".format(card.number, card.color.name) for card in totem.stacks[0].cards])
            stackString1 = " ".join(
                ["{:1}:{:6}".format(card.number, card.color.name) for card in totem.stacks[1].cards])
            print("\n\t\t\t{:30} = TOTEM {} = {:30}".format(stackString0, i, stackString1))
            i += 1

    def showHands(self):
        for player in self.players:
            handString = player.name + "\t\t" + " ".join(
                ["{:1}:{:6}".format(card.number, card.color.name) for card in player.hand])
            print(handString)

    def getPlayerInput(self):
        cardToPlay = int(input())
        totemToPlay = int(input())
        return Move(self.activePlayer, self.activePlayer.hand[cardToPlay], self.totems[totemToPlay])

    def run(self):
        self.shuffle()
        self.distribute()
        self.selectFirstPlayer()
        while not self.isFinished():
            self.displayBoard()
            move = None
            while move is None or not self.isMoveValid(move):
                move = self.getPlayerInput()
            self.makeMove(move)
            self.history.append(move)
            self.drawCard()
            self.changePlayer()

    def getPlayerByName(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def makeMove(self, move):
        move.totem.addCard(move.player.id, move.card)
        self.activePlayer.playCard(move.card)
        move.totem.updateStatus()

    def drawCard(self):
        if len(self.deck) > 0:
            self.activePlayer.takeCard(self.deck[0])
            del self.deck[0]

    def changePlayer(self):
        if self.activePlayer.id == 1:
            self.activePlayer = self.players[0]
        else:
            self.activePlayer = self.players[1]

    def isMoveValid(self, move):
        return True

    def isFinished(self):
        return False

    def shuffle(self):
        random.shuffle(self.deck)

    def distribute(self):
        for i in range(6 * len(self.players)):
            self.players[i % 2].takeCard(self.deck[0])
            del self.deck[0]

    def selectFirstPlayer(self):
        first = random.randrange(len(self.players))
        self.activePlayer = self.players[first]


class Combination(enum.Enum):
    Sum = 0
    Straight = 1
    Color = 2
    Brelan = 3
    ColorStraight = 4


class Color(enum.Enum):
    Red = 0
    Blue = 1
    Green = 2
    Purple = 3
    Yellow = 4
    Brown = 5