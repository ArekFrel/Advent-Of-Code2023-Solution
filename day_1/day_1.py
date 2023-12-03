FILE = '../inputs/input_01.txt'
# FILE = '../inputs/test_input_01.txt'

NUMBER_DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

MIN_LEN = min([len(key) for key in NUMBER_DICT])


def solve(part):
    value = 0
    with open(FILE, 'r', encoding='utf-8') as my_input:
        if part == 1:
            for line in my_input:
                value += get_number_part_1(line)
        if part == 2:
            for line in my_input:
                value += get_number_part_2(line)
    return value


def text_into_number(text):

    changed_from_start, changed_from_end = False, False
    i, j = 0, 1
    while not changed_from_start and i <= len(text):
        if text[i].isdigit():
            changed_from_start = True
            break
        if i >= MIN_LEN - 1:
            for key in NUMBER_DICT:
                if key in text[:i + 1]:
                    text = text.replace(key, f'{NUMBER_DICT.get(key)}{key}', 1)
                    changed_from_start = True
                    break
        i += 1

    while not changed_from_end and j <= len(text):
        if text[-j].isdigit():
            changed_from_end = True
            break
        if j >= MIN_LEN - 1:
            for key in NUMBER_DICT:
                if key in text[-(j + 1):]:
                    text = text[:len(text) - (j + 1)] + text[-(j + 1):].replace(key, f'{key}{NUMBER_DICT.get(key)}')
                    changed_from_end = True
                    break
        j += 1

    return text


def get_number_part_1(text):

    array = [_ for _ in text]
    digits = list(filter(lambda x: x.isdigit(), array))
    first_and_last_digit = [digits[0], digits[-1]]
    number = int(''.join(first_and_last_digit))
    return number


def get_number_part_2(text):

    text = text_into_number(text)
    array = [_ for _ in text]
    digits = list(filter(lambda x: x.isdigit(), array))
    first_and_last_digit = [digits[0], digits[-1]]
    number = int(''.join(first_and_last_digit))
    return number


def main():

    # print("Result of part 1 is:", solve(1))
    print("Result of part 2 is:", solve(2))


if __name__ == '__main__':
    main()
