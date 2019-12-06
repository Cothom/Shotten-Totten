class Player:
    def __init__(self, id, name=None):
        self.id = id
        self.name = name if name is not None else "Player" + str(id)
        self.hand = []

    def takeCard(self, card):
        self.hand.append(card)
        self.hand.sort(key=lambda card: card.number)

    def playCard(self, card):
        self.hand.remove(card)
