####blackjack


class blackjack:
    def __init__(self, card, card_ace):
        self.card = card
        self.value = [0, 0]
        self.ace = card_ace
        self.hand = []
        self.O_hand = []

    def get_hand(self):

        while len(self.hand) > 3:
            self.card = input("Enter the cards that you have obtained in your first hand") ######setup that concerns the user's hand
            self.hand.append(self.card)
        while len(self.O_hand) > 2:

            self.card = input("Enter the card that your opponent has") #####setup that concerns the opponent's hand
            self.O_hand.append(self.card)

    def get_value(self):
        for card in self.hand:
            if (card != "Ace") or (card != "ace"):
                self.value[0] += int(card)
                self.value[1] += int(card)
            else:
                self.value[0] += 1
                self.value[1] += 11
