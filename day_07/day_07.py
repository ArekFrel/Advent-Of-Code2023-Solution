import string

DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2


class Hand:

    type_of_cards = [
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'T',
        'J',
        'Q',
        'K',
        'A',
    ]
    all_hands = []

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.type = self.type_of_hand()
        Hand.all_hands.append(self)
        self.rank = None
        self.coded_hand = self.code_name()

    def code_name(self):
        values = [sign for sign in string.ascii_lowercase[0:len(Hand.type_of_cards) + 1]]
        dictionary = {k: v for k, v in zip(Hand.type_of_cards, values)}
        return ''.join([dictionary.get(sign) for sign in self.cards])

    # @staticmethod
    # def compare_card(card_1, card_2):
    #     rank_card_1 = Hand.type_of_cards.index(card_1)
    #     rank_card_2 = Hand.type_of_cards.index(card_2)
    #
    #     if rank_card_1 < rank_card_2:
    #         return card_1
    #     if rank_card_1 > rank_card_2:
    #         return card_2
    #     if rank_card_1 == rank_card_2:
    #         return 0

    def type_of_hand(self):
        diff_cards = list(set([x for x in self.cards]))
        card_counter = []
        for diff_card in diff_cards:
            if SOLVE_PART == 2:
                if diff_card != 'J':
                    card_counter.append(self.cards.count(diff_card))
                else:
                    card_counter.append(0)
            else:
                card_counter.append(self.cards.count(diff_card))
        if SOLVE_PART == 2:
            if self.cards.count('J') > 0:
                card_counter.sort(reverse=True)
                if len(card_counter) == 0:
                    a = 0
                card_counter[0] += self.cards.count('J')

        if 5 in card_counter:
            return 0
        if 4 in card_counter:
            return 1
        if 3 in card_counter and 2 in card_counter:
            return 2
        if 3 in card_counter and 1 in card_counter:
            return 3
        if card_counter.count(2) == 2:
            return 4
        if 2 in card_counter and card_counter.count(1) == 3:
            return 5
        if card_counter.count(1) == 5:
            return 6

    @staticmethod
    def rank_of_hand():
        hand_rank = 1
        for type in list(range(6, -1, -1)):
            one_type_hands = list(filter(lambda x: x.type == type, Hand.all_hands))
            one_type_hands.sort(key=lambda x: x.coded_hand)
            for hand in one_type_hands:
                hand.rank = hand_rank
                hand_rank += 1

    @staticmethod
    def count_bid():
        result = 0
        for hand in Hand.all_hands:
            result += hand.rank * hand.bid
        return result


def solve_01():
    with open(FILE, 'r', encoding='utf-8') as my_input:
        for line in my_input:
            hand, bid = line.rstrip().split(' ')
            new_hand = Hand(hand, bid)
    Hand.rank_of_hand()
    print(f'Result of day {DAY} part {SOLVE_PART} is {Hand.count_bid()}.')


def solve_02():

    Hand.type_of_cards = [
        'J',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'T',
        'Q',
        'K',
        'A',
    ]
    solve_01()


def main():

    if SOLVE_PART == 1:
        solve_01()
    if SOLVE_PART == 2:
        solve_02()


if __name__ == '__main__':
    main()
