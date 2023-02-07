###blackjack


class blackjack:
    def __init__(self, card, card_ace):
        self.card = card
        self.value = [0, 0]
        self.O_value = [0, 0]
        self.ace = card_ace
        self.hand = []
        self.O_hand = []

    def get_hand(self):

        while len(self.hand) > 3:
            self.card = input("Enter the cards that you have obtained in your first hand")
            self.hand.append(self.card)
        while len(self.O_hand) > 2:

            self.card = input("Enter the card that your opponent has")
            self.O_hand.append(self.card)

    def get_value(self):
        for card in self.hand:
            if (card != "Ace") or (card != "ace"):
                self.value[0] += int(card)
                self.value[1] += int(card)
            else:
                self.value[0] += 1
                self.value[1] += 11

        for O_card in self.O_hand:
            if (O_card != "Ace") or (O_card != "ace"):
                self.O_value[0] = int(O_card)
            else:
                self.value[0] = 1
                self.value[1] = 11
    def decision(self):
        distance = []
        if self.value == [21,21]:
            print("Congratulations, no further instructions will be given, you already won!")
        elif (self.value == [11,11]) or (self.value == [10,10]):
            print("Unless you cannot, consider a double down, you will most likely hit 21.")
        else:
             while self.value[0] < 14:
                 print("Hit!")
            
                
