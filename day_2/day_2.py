FILE = '../inputs/input_02.txt'
# FILE = '../inputs/test_input_02.txt'
DAY = 2
SOLVE_PART = 2


def solve(part):
    data = parse_data(FILE)
    for i in range(len(data)):
        data[i] = data[i].split(',')
    if part == 1:
        sum_of_impossible_ids = 0
        sum_of_all_ids = 0
        for i, games in enumerate(data, 1):
            sum_of_all_ids += i
            for game in games:
                val, col = game.split(' ')
                if col == "blue" and int(val) > 14:
                    sum_of_impossible_ids += i
                    break
                if col == "green" and int(val) > 13:
                    sum_of_impossible_ids += i
                    break
                if col == "red" and int(val) > 12:
                    sum_of_impossible_ids += i
                    break
        return sum_of_all_ids - sum_of_impossible_ids

    if part == 2:
        result = 0
        for i, games in enumerate(data, 1):
            max_red, max_green, max_blue = 0, 0, 0
            for game in games:
                val, col = game.split(' ')
                val = int(val)
                if col == "blue":
                    if not max_blue or val > max_blue:
                        max_blue = val
                    continue
                if col == "green" :
                    if not max_green or val > max_green:
                        max_green = val
                    continue
                if col == "red":
                    if not max_red or val > max_red:
                        max_red = val
                    continue
            result += max_blue * max_green * max_red
        return result


def parse_data(file):
    with open(file, 'r', encoding='utf-8') as my_input:
        data = [line.replace(', ', ',').replace('; ', ';').replace(': ', ':')for line in my_input]
        for i in range(len(data)):
            games = ','.join(data[i].split(':')[1].strip().split(';'))
            data[i] = games
    return data


def main():
    print(f'result of day{DAY} part {SOLVE_PART} is {solve(SOLVE_PART)}')


if __name__ == '__main__':
    main()
