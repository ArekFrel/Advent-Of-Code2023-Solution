FILE = 'input_011.txt'
# FILE = 'test_input.txt'

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


def solve(part):
    file = FILE
    value = 0
    with open(file, 'r', encoding='utf-8') as input:
        if part == 1:
            for line in input:
                value += get_2_digit_number_1(line)
        if part == 2:
            for line in input:
                value += get_2_digit_number_2(line)
    return value


def text_into_number(text):

    number_dict = NUMBER_DICT
    min_len = min([len(key) for key in NUMBER_DICT])
    changed_from_start, changed_from_end = False, False
    i, j = 0, 1
    while not changed_from_start and i <= len(text):
        if text[i].isdigit():
            changed_from_start = True
            break
        if i >= min_len - 1:
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
        if j >= min_len - 1:
            for key in NUMBER_DICT:
                if key in text[-(j + 1):]:
                    text = text[:len(text) - (j + 1)] + text[-(j + 1):].replace(key, f'{key}{NUMBER_DICT.get(key)}')
                    changed_from_end = True
                    break
        j += 1

    return text


def get_2_digit_number_1(text):

    array = [_ for _ in text]
    digits = list(filter(lambda x: x.isdigit(), array))
    first_and_last_digit = [digits[0], digits[-1]]
    number = int(''.join(first_and_last_digit))
    return number


def get_2_digit_number_2(text):

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
