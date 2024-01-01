import math

DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1


def get_data(text):
    while '  ' in text:
        text = text = text.replace('  ', ' ')
    return [int(num) for num in text.split(' ')]


def solve():
    with open(FILE, 'r', encoding='utf-8') as my_input:
        times = get_data(my_input.readline().split(':')[1].strip())
        records = get_data(my_input.readline().split(':')[1].strip())

    pairs = list(zip(times, records))
    values = []
    for pair in pairs:
        values.append(calc_race(pair))

    print(f'Result of day {DAY} part {SOLVE_PART} is {math.prod(values)}.')


def calc_race(pair):
    time, record = pair
    pivot = math.ceil(time / 2)
    not_even = not((time + 1) % 2 == 0)
    ways_to_win = 0
    while pivot * (time - pivot) > record:
        ways_to_win += 1
        pivot += 1
    if not_even:
        ways_to_win = ways_to_win * 2 - 1
    else:
        ways_to_win *= 2
    return ways_to_win


def solve_02():
    pass


def main():
    if SOLVE_PART == 1:
        solve()
    if SOLVE_PART == 2:
        solve_02()


if __name__ == '__main__':
    main()
