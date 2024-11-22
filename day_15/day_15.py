DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1
MY_DICT = []


def main():
    if SOLVE_PART == 1:
        with open(FILE, 'r', encoding='utf-8-sig') as my_input:
            line = my_input.readline()
            codes = line.split(',')
            big_results = []
            for code in codes:
                result = 0
                for sign in code:
                    a = ord(sign) + result
                    result = (17 * a) % 256
                big_results.append(result)
            print(f'The Result of part {SOLVE_PART} is {sum(big_results)}')


if __name__ == '__main__':
    main()
