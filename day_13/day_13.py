DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2


def main():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:

        # a = len(input)
        b = my_input.readlines()
        counter = 1
        rows = []
        ans = 0
        for i, line in enumerate(b):
            row = [_ for _ in line if _ != '\n']
            if row not in (['\n'], []):
                rows.append(row.copy())
            if line == '\n' or i == len(b) - 1:
                add = calculate(rows, 'rows')
                if not add:
                    cols = [[x[i] for x in rows] for i in range(len(rows[0]))]
                    add += calculate(cols, 'cols')
                ans += add
                if add <99:
                    for r in rows:
                        print(''.join(r))
                    print(f'result is {add} \n no of rows: {len(rows)} \n no of cols: {len(rows[0])}')
                    print('\n')
                counter += 1
                rows = []
                # continue
    print(f'The Result is:   {ans}')

def calculate(arr, arg):
    a = len(arr)
    for i in range(a - 1):
        if SOLVE_PART == 1:
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
                        return 100 * (i +1)
                    if arg == 'cols':
                        return  i + 1

        if SOLVE_PART == 2:
            if arr[i] == arr[i + 1] or find_smudge(arr[i], arr[i + 1]):
                more = min(i, a - 2 - i)
                if arr[i] == arr[i + 1]:
                    for _ in range(1, more + 1):
                        one = arr[i - _]
                        two = arr[_ + 1 + i]
                        if not find_smudge(one, two):
                            more -= 1
                    if more == 1:
                        if arg == 'rows':
                            return 100 * (i + 1)
                        if arg == 'cols':
                            return i + 1
                if find_smudge(arr[i], arr[i + 1]):
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


def find_smudge(arr1, arr2)-> bool:
    score  = len(arr1)
    for i, j in zip(arr1, arr2):
        if i == j:
            score -= 1
    return score == 1


if __name__ == '__main__':
    main()


