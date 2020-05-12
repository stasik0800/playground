import random

class Card():
    def __init__(self,suit,val):
        self.suit = suit
        self.val = val

    def showCard(self):
        return (f"{self.suit}|{self.val}")

    def getCard(self):
        return {'val':self.val,'suit':self.suit}

class Deck():
    def __init__(self):
        self.deck =[]
        self._build()
        self._shuffle()

    def _build(self):
        for t in ['♣', '♦', '♥', '♠']:
            for n in range(1,14):
                self.deck.append(Card(t,n))

    def _shuffle(self):
        for i in range(0,len(self.deck)):
            rand = random.randint(0,i)
            self.deck[rand] ,self.deck[i] = self.deck[i] ,self.deck[rand]

    def drawCard(self):
        return self.deck.pop()

    def CheckDeckSize(self):
        d = {}
        for n in self.deck:
            if n.suit in d:
                d[n.suit]+=1
            else :
                d[n.suit]=1
        print (d)

    def showDeck(self):
        for card in self.deck:
            card.showCard()

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def addCard(self,deck):
        self.hand.append(deck.drawCard())

    def putCard(self,inx):
        return self.hand.pop(inx)

    def showHand(self):
        for inx,card in enumerate(self.hand):
            print(f'{self.name} , {card.showCard()} , inx:{inx}')

    @property
    def getCards(self):
        return [card.getCard() for card in self.hand]






