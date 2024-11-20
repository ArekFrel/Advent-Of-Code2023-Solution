DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2


def main():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:

        # a = len(input)
        b = my_input.readlines()
        rows = []
        ans = 0
        counter = 1
        for i, line in enumerate(b):

            row = [_ for _ in line if _ != '\n']
            if row not in (['\n'], []):
                rows.append(row.copy())
            if line == '\n' or i == len(b) - 1:
                add = calculate(rows, 'rows', SOLVE_PART)
                if add == 0:
                    cols = [[x[i] for x in rows] for i in range(len(rows[0]))]
                    add += calculate(cols, 'cols', SOLVE_PART)
                ans += add
                print(f'{counter} answer: {add}')
                counter += 1
                rows = []
                continue

    print(f'The Result is:   {ans}')


def calculate(arr, arg, solve_part):
    a = len(arr)

    for i in range(a - 1):

        if solve_part == 1:
            if arr[i] == arr[i + 1]:
                more = min(i, a - 2 - i)
                for _ in range(1, more + 1):
                    one = arr[i - _]
                    two = arr[_ + 1 + i]
                    if one != two:
                        break
                    more -= 1
                if more == 0:
                    if arg == 'rows':
                        return 100 * (i + 1)
                    if arg == 'cols':
                        return i + 1

        if solve_part == 2:
            if arr[i] == arr[i + 1]:
                more = min(i, a - 2 - i)
                is_smuge = False
                for _ in range(1, more + 1):
                    one = arr[i - _]
                    two = arr[_ + 1 + i]
                    if one == two:
                        more -= 1
                    if find_smuge(one, two):
                        more -= 1
                        is_smuge = True
                if more == 0 and is_smuge:
                    if arg == 'rows':
                        return 100 * (i + 1)
                    if arg == 'cols':
                        return i + 1
            if find_smuge(arr[i], arr[i + 1]):
                more = min(i, a - 2 - i)
                for _ in range(1, more + 1):
                    one = arr[i - _]
                    two = arr[_ + 1 + i]
                    if one == two:
                        more -= 1
                if more == 0:
                    if arg == 'rows':
                        return 100 * (i + 1)
                    if arg == 'cols':
                        return i + 1
    return 0


def find_smuge(arr_1, arr_2) -> bool:
    a = len(arr_1)
    for i, j in zip(arr_1, arr_2):
        if i == j:
            a -= 1
    return a == 1


if __name__ == '__main__':
    main()


