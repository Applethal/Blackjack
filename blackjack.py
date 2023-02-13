###blackjack


class blackjack:
    def __init__(self):

        self.value = [0, 0]
        self.O_value = [0, 0]

        self.hand = []
        self.O_hand = []

    def get_hand(self):

        while len(self.hand) < 2:
            self.card = input("Enter the cards that you have obtained in your first hand")
            self.hand.append(self.card)

        self.card = input("Enter the card that your opponent has")
        self.O_hand.append(self.card)

    def get_value(self):
        self.value = [0, 0]
        self.O_value = [0]
        for card in self.hand:
            if "ace" not in card.lower():
                self.value[0] += int(card)
                self.value[1] += int(card)
            else:
                self.value[0] += 1
                self.value[1] += 11
        print("Your value is  ", self.value)
        for card in self.O_hand:
            if "ace" not in card.lower():
                self.O_value[0] = int(card) + 8

            else:
                self.O_value[0] = 1 + 7
                self.O_value[1] = 11 + 7
        print("Your  Opponent's value is  ", self.O_value)

    def luck_computation(self):
        i = 0

        n = self.value[0]
        O_n = self.O_value[0]
        distance_to_21 = []
        O_distance_to_21 = []
        distances = 0
        sum_chances = 0
        sum_chances_d = 0
        while n + i < 21:
            distances = 21 - n - i
            distance_to_21.append(distances)
            i += 1
        i = 0
        distances = 0

        while n + i < 21:
            distances = 21 - O_n - i
            O_distance_to_21.append(distances)
            i += 1
            if O_distance_to_21[-1] == 0:
                O_distance_to_21.pop()
                break

        for luck in distance_to_21:

            if luck == 10:
                chance = (16 -
                          (self.hand.count(10) + self.O_hand.count(10))) / (52 - (len(self.O_hand) + len(self.hand)))
            else:
                chance = (4 - (self.hand.count(luck) +
                               self.O_hand.count(luck))) / (52 - (len(self.O_hand) + len(self.hand)))

            sum_chances += chance

        for luck_d in O_distance_to_21:

            if luck_d == 10:
                chance_d = (16 -
                            (self.hand.count(10) + self.O_hand.count(10))) / (52 - (len(self.O_hand) + len(self.hand)))
            else:
                chance_d = (4 - (self.hand.count(luck_d) +
                                 self.O_hand.count(luck_d))) / (52 - (len(self.O_hand) + len(self.hand)))

            sum_chances_d += chance_d

        return sum_chances_d, sum_chances

    def decision(self):
        while self.value[0] < 22:
            if self.value[-1] == 21:
                print("Congratulations, no further instructions will be given, you already have won!")
                break
            elif (self.value == [11, 11]) or (self.value == [10, 10]):
                print("Unless you cannot, consider a double down, you will most likely hit 21.")
                self.card = input("Enter the card that you have obtained now")
                self.hand.append(self.card)
                self.get_value()
            elif self.value[1] > 12:
                v1, v2 = self.luck_computation()

                if v1 > v2:
                    print("If you hit, chances are that you would not bust if you compare yours with the dealer")
                    self.card = input("Enter the card that you have obtained now")
                    self.hand.append(self.card)
                    self.get_value()
                else:
                    print("Hitting is not advised in this case, Hold it!")
                    break
            else:
                print("Hit!!!!")
                self.card = input("Enter the card that you have obtained now")
                self.hand.append(self.card)
                self.get_value()


def main():
    gamble = blackjack()
    gamble.get_hand()
    gamble.get_value()
    gamble.luck_computation()
    gamble.decision()


main()
