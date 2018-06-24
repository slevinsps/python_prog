class Card(object):
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank, suit, face = True):
        self.rank = rank
        self.suit = suit
        self.face = face

    def __str__(self):
        if self.face:
            r = self.rank + self.suit
        else:
            r = 'XX'
        return r
    def flip(self):
        self.face = not self.face


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + ' '
        else:
            rep = 'пусто'
        return rep

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def give(self, card, massiv2):
        self.cards.remove(card)
        massiv2.add(card)


class Deck(Hand):
    def populate(self):
        for i in Card.SUITS:
            for j in Card.RANKS:
                self.add(Card(j, i))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, spisok, k=1):
        for i in range(k):
            for j in spisok:
                if self.cards:
                    Top = self.cards[0]
                    self.give(Top, j)
                else:
                    print('Карты закончились!')
if __name__ == "__main__":
    print('Это модуль, содержащий классы для карточных игр.')
    input('\n\nНажмите Enter, чтобы выйти')
