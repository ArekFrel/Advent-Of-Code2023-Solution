DAY = '04'
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2
with open(FILE, 'r', encoding='utf-8') as my_input:
    ARRAY = [line for line in my_input]


def remove_double_space(text):
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text


def solve_part_1():
    score = []
    for line in ARRAY:
        line = remove_double_space(line)
        line = line[line.index(':') + 1:]
        winning_numbers, shoots = line.split('|')
        winning_numbers = [int(_) for _ in winning_numbers.strip().split(' ')]
        shoots = [int(_) for _ in shoots.strip().rstrip().split(' ')]
        result = 0
        for shoot in shoots:
            if shoot in winning_numbers:
                result += 1
        if result > 0:
            score.append(1 * 2 ** (result - 1))

    print(f'Result of day {DAY} part {SOLVE_PART} is {sum(score)}.')


class Card:

    cards = []

    def __init__(self, index, shoots, winning_numbers):
        self.index = index
        self.shoots = shoots
        self.winning_numbers = winning_numbers
        self.counter = 1
        self.scratched = False
        Card.cards.append(self)

    def count_points(self):
        points = len(list(filter(lambda x: x in self.winning_numbers, self.shoots)))
        return points

    def add_cards(self):
        if self.index == 5:
            a = 0
        number_of_cards_to_add = self.count_points()
        if number_of_cards_to_add > 0:
            for i in range(self.index, self.index + number_of_cards_to_add ):
                Card.card_by_id(i).counter += self.counter
            self.mark_as_scratched()

    def mark_as_scratched(self):
        self.scratched = True

    @staticmethod
    def card_by_id(index):
        if index > len(Card.cards):
            return None
        return Card.cards[index]

    @staticmethod
    def scratch():
        for card in Card.cards:
            if not card.scratched:
                card.add_cards()

    @staticmethod
    def count_cards():
        return sum(list(map(lambda x: x.counter, Card.cards)))


def solve_part_2():

    def create_cards():
        for index, line in enumerate(ARRAY, 1):
            line = remove_double_space(line)
            line = line[line.index(':') + 1:]
            winning_numbers, shoots = line.split('|')
            winning_numbers = [int(_) for _ in winning_numbers.strip().split(' ')]
            shoots = [int(_) for _ in shoots.strip().rstrip().split(' ')]
            Card(index, winning_numbers, shoots)

    def calculate():
        Card.scratch()
        return Card.count_cards()

    create_cards()
    result = calculate()
    print(f'Result of day {DAY} part {SOLVE_PART} is {result}.')
    return result


def main():
    if SOLVE_PART == 1:
        solve_part_1()
    if SOLVE_PART == 2:
        solve_part_2()


if __name__ == '__main__':
    main()


