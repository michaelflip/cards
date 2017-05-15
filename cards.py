import random

def main():
    game = Game()
    game.run()


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

class Game:
    def __init__(self):
        self.deck = Deck()

    def run(self):
        print 'Welcome to my Card Game'
        print 'I will now shuffle cards.'
        self.deck.shuffle()
        self.hand = []
        self.hand.append(self.deck.pop())
        self.hand.append(self.deck.pop())
        while True:
            print self.hand
            answer = raw_input('Would you like to [H]it or [S]tay?')
            if answer == 'H':
                print 'Dealing you another card'
                self.hand.append(self.deck.pop())
            elif answer == 'S':
                print 'You\'re staying'
                break
            else:
                print 'I don\'t understand.'
            total = 0
            for card in self.hand:
                total = total + card.number
            if total > 21:
                print self.hand
                print 'Busted!'
                exit()

        self.dealer_hand = []
        self.dealer_hand.append(self.deck.pop())
        self.dealer_hand.append(self.deck.pop())
        print 'The dealer has:'
        print self.dealer_hand
        dealer_total = 0
        for card in self.dealer_hand:
            dealer_total = dealer_total + card.number
        player_total = 0
        for card in self.hand:
            player_total = player_total + card.number
        if player_total > dealer_total or dealer_total > 21:
            print 'You win!'
        else:
            print 'You lose!'


if __name__ == '__main__':
    main()
