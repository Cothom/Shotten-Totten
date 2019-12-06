from Game import Combination


class Stack:
    def __init__(self):
        self.cards = []
        self.combination = None

    def updateCombination(self):
        if self.isSum():
            self.combination = Combination.Sum
        if self.isStraight():
            self.combination = Combination.Straight
        if self.isColor():
            self.combination = Combination.Color
        if self.isBrelan():
            self.combination = Combination.Brelan
        if self.isColorStraight():
            self.combination = Combination.ColorStraight

    def isSum(self):
        return len(self.cards) > 0

    def isStraight(self):
        return len(self.cards) == 3 and \
               self.cards[0].number == self.cards[1].number - 1 == self.cards[2].number - 2

    def isColor(self):
        return all(
            [True if card.color == self.cards[0].color else False for card in self.cards])

    def isBrelan(self):
        return len(self.cards) == 3 and all(
            [True if card.number == self.cards[0].number else False for card in self.cards])

    def isColorStraight(self):
        return self.isColor() and self.isStraight()
