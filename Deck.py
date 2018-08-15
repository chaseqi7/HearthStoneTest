import Card
import random


class Deck:
    def __init__(self, size):
        self.card_holder = []

        for i in range(size):
            self.card_holder.append(Card.Card(random.randint(1, 10), random.randint(1, 10)))

    def get_deck(self):
        return self.card_holder
