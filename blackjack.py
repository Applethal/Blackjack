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
                self.O_value[0] = 1
                self.O_value[1] = 11

    def decision(self):
        while self.value[0] < 22:
            if self.value[-1] == 21:
                print("Congratulations, no further instructions will be given, you already won!")
            elif (self.value == [11, 11]) or (self.value == [10, 10]):
                print("Unless you cannot, consider a double down, you will most likely hit 21.")
            elif self.value[1] > 14:
                print("Hit")
                self.card = input("Enter the card that you have obtained now")
                self.hand.append(self.card)
                self.get_value()
    
    def luck_computation(self):
        i = 0
        n = self.value[0]
        O_n = self.O_value[0]
        distance_to_21 = []
        O_distance_to_21 = []
        distances = 0
        while n + i < 22:
            distances = 21 - n - i
            distance_to_21.append(distances)
            distances = 0
            distances = 11 - O_n - i 
            O_distance_to_21.append(distances)
            i += 1
        
        for luck in distances:
            if self.hand[0] == distances[0] or
            
