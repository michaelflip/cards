import random

def main():
    deck = Deck()
    deck.shuffle()
    deck.pop()
    print deck.pop()


def poop():
    return 'i pooped'

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return '{} - {}'.format(self.suit, self.number)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['H', 'C', 'S', 'D']:
            for number in range(14):
                self.cards.append(Card(number, suit))

    def __repr__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()

if __name__ == '__main__':
    main()
