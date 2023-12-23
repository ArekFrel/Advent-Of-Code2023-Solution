DAY = '04'
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1
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








def solve_part_2():
    pass




def main():
    if SOLVE_PART == 1:
        solve_part_1()
    if SOLVE_PART == 2:
        solve_part_2()


if __name__ == '__main__':
    main()


