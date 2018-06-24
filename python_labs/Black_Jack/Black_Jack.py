import cards, games

class BJcard(cards.Card):
    ACE_VAlUE = 1
    @property
    def value(self):
        if self.face:
            v = BJcard.RANKS.index(self.rank)+1
            if v>10:
                v = 10
            else:
                v = None
            return v

class BJdeck(cards.Deck):
    def populate(self):
        for i in BJcard.SUITS:
            for j in BJcard.RANKS:
                self.cards.append(BJcard(j, i))

class BJhand(cards.Hand):
    def __init__(self,name):
        super(BJhand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ':\t' +super(BJhand, self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        ace = False
        for card in self.cards:
            if card.value == BJcard.ACE_VAlUE:
                ace = True
        if ace and t<=11:
            t += 10
        return t
    def is_busted(self):
        return self.total > 21

class BJplayer(BJhand):
    def is_hit(self):
        res = games.ask('\n'+self.name + ' будете брать еще карты? (Y/N)')
        return res == 'y'
    def bust(self):
        print(self.name, 'перебрал')
        self.lose()
    def lose(self):
        print(self.name, 'проиграл')
    def win(self):
        print(self.name, 'выиграл')
    def push(self):
        print(self.name, 'сыграл в ничью')

class BJdealer(BJhand):
    def is_hit(self):
        return self.total <17
    def bust(self):
        print(self.name, 'перебрал')

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
class BJgame(object):
    def __init__(self,names):
        self.players = []
        for name in names:
            player = BJplayer(name)
            self.players.append(player)
        self.dealer = BJdealer('Dealer')
        self.deck = BJdeck()
        self.deck.populate()
        self.deck.shuffle()
    @property
    def still(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    def __additional_cards(self,player):

        while not player.is_busted() and player.is_hit():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    def play(self):
        self.deck.deal(self.players +[self.dealer],k = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still:
                    player.win()
            else:
                for player in self.still:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()
def main():
    print('Добро пожаловать за игровой стол Блек-джека!\n')
    names = []
    number = games.ask_number('Сколько всего игроков (1-7): ',low = 1, high = 8)
    for i in range(number):
        name = input('Введите имя: ')
        names.append(name)
        print()
    game = BJgame(names)
    again = None
    while again != 'n':
        game.play()
        again = games.ask('\nХотите сыграть еще раз?')
        main()
    input('\nНажмите Enter, чтобы выйти.')

main()