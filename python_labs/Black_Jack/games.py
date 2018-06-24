class Player(object):
    def __init__(self,name, score = 0):
        self.score = score
        self.name = name
    def __str__(self):
        rep = self.name + ':\t' + str(self.score)
        return rep
def ask(quest):
    t = None
    while t not in ('y','n'):
        print(quest)
        t = input()
    return t
def ask_number(quest,low,high):
    g = None
    while g not in range(low,high):
        print(quest)
        g = int(input())
    return g
if __name__ == "__main__":
    print('Это модуль, содержащий классы для карточных игр.')
    input('\n\nНажмите Enter, чтобы выйти')

