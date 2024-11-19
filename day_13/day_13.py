DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1


def main():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:

        # a = len(input)
        b = my_input.readlines()
        rows = []
        ans = 0
        for i, line in enumerate(b):
            if i == 14:
                t = 0
            row = [_ for _ in line if _ != '\n']
            if row not in (['\n'], []):
                rows.append(row.copy())
            if line == '\n' or i == len(b) - 1:
                add = calculate(rows, 'rows')
                if add == 0:
                    cols = [[x[i] for x in rows] for i in range(len(rows[0]))]
                    add += calculate(cols, 'cols')
                ans += add
                print(f'answer is {add}')
                rows = []
                continue

    print(f'The Result is:   {ans}')

def calculate(arr, arg):
    a = len(arr)
    if arg == 'cols':
        t = 0
    for i in range(a - 1):
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
    return 0


if __name__ == '__main__':
    if SOLVE_PART == 1:
     main()


