from Stack import Stack


class Totem:
    def __init__(self):
        self.stacks = [Stack(), Stack()]
        self.winner = None

    def addCard(self, playerId, card):
        self.stacks[playerId].cards.append(card)
        self.stacks[playerId].cards.sort(key=lambda card: card.number)

    def updateStatus(self):
        for stack in self.stacks:
            stack.updateCombination()
