from StasProj.cardsBase.Infrastraction import Deck, Player, Card


class DurakDeck(Deck):
    kozer=''
    def __init__(self):
        super(DurakDeck, self).__init__()
        self._setKozer()
    def _setKozer(self):
        DurakDeck.kozer =  self.deck[0].suit



class DurakPlayer(Player):
    def __init__(self,name):
        super(DurakPlayer, self).__init__(name)
    def takeCards(self,deck,amtCards):
        for x in range(0,amtCards):
            self.addCard(deck)



class Bita:
    def __init__(self):
        self.bita = []

    def toBita(self, card):
        if isinstance(card,Card):
            self.bita.append(card)

    def showBita(self):
        for cards in self.bita:
            print(cards.showCard())
        print(f'Total {len(self.bita)} cards in Bita')


class Table:
    __firstDraw=6
    def __init__(self,players):
        self.players = players
        self.deck = DurakDeck()
        self.bita = Bita()
        self.joinToTable()
        print(f"Kozer: {self.deck.kozer}")

    def joinToTable(self):
        for player in self.players:
            player.takeCards(self.deck,Table.__firstDraw)
            print(player.name , ' joined to table')

    def whichPlayerStarts(self):
        l =[]
        for player in self.players:
            [l.append({'player':player.name,'val':card['val'],'suit':card['suit']}) for card in player.getCards if card['suit']==self.deck.kozer]
        data = max(l,key=lambda x:int(x['val']))
        print(f"{data['player']} Start , holds {data['suit']}|{data['val']}")



class Round:
    id=1
    rules ={}









stas = DurakPlayer('stas')
moti = DurakPlayer('moti')
kobi = DurakPlayer('kobi')
print('-----------------------')
table = Table([stas,kobi,moti])
print('-----------------------')
table.whichPlayerStarts()
moti.showHand()
stas.showHand()
kobi.showHand()
