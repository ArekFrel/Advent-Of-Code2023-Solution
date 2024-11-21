DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2
MY_DICT = {}


def main():

    rows = []
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        for line in my_input:
            rows.append(line.rstrip())

    if SOLVE_PART == 1:
        cols = [[_[i] for _ in rows] for i in range(len(rows[0]))]
        for i in range(len(cols)):
            cols[i] = fall_rocks(cols[i])
        rows = [[_[i] for _ in cols] for i in range(len(cols[0]))]
    if SOLVE_PART == 2:
        rows = cycle(rows, 1000)
    nums = [_ for _ in range(len(rows[0]), 0, -1)]
    result = 0

    for i, j in zip(rows, nums):
        result += i.count('O') * j
    print(f'The result is {result}')


def transform_arr(arr):
    return [[_[i] for _ in arr] for i in range(len(arr[0]))]


def cycle(arr, rounds):
    results = []
    nums = [_ for _ in range(len(arr[0]), 0, -1)]
    arr_set = []
    rnd_num = 1
    for rnd in range(1, rounds + 1):
        result = 0
        arr = go_north(arr)
        arr = go_west(arr)
        arr = go_south(arr)
        arr = go_east(arr)

        for i, j in zip(arr, nums):
            result += i.count('O') * j
        results.append(result)
        # print(f'The result after round {rnd} is {result}')
        if arr not in arr_set:
            arr_set.append(arr)
        else:
            break
        # results.append(result)
        rnd_num += 1
    # print(rnd_num)
    first = arr_set.index(arr) + 1
    loop = rnd_num - first
    a = (1000000000-first) % loop + first
    print(f'{rnd_num=}')
    print(f'{first=}')
    print(f'{loop=}')
    print(f'{a=}')
    print(results[a])
    return arr


def calculate_load(arr):
    result = 0
    nums = [_ for _ in range(len(arr[0]), 0, -1)]
    for i, j in zip(arr, nums):
        result += i.count('O') * j
    return result


def fall_rocks(col):
    col = ''.join(col)
    segments = col.split('#')
    result = []
    for segment in segments:
        a = len(segment)
        if a == 0:
            result.append('')
            continue
        b = segment.count('O')
        seg = 'O' * b + '.' * (a - b)
        result.append(seg)
        t = 0
    col = '#'.join(result)
    col = [_ for _ in col]
    return col


def go_north(arr) -> list:
    new_arr = []
    for i in range(len(arr[0])):
        col = ''.join([row[i] for row in arr])
        segments = col.split('#')
        new_col = []
        for segment in segments:
            a = len(segment)
            if a == 0:
                new_col.append('')
                continue
            b = segment.count('O')
            seg = 'O' * b + '.' * (a - b)
            new_col.append(seg)
        new_col = '#'.join(new_col)
        new_arr.append(list(new_col))
    return transform_arr(new_arr)


def go_west(arr) -> list:
    new_arr = []
    for row in arr:
        row = ''.join(row)
        segments = row.split('#')
        new_col = []
        for segment in segments:
            a = len(segment)
            if a == 0:
                new_col.append('')
                continue
            b = segment.count('O')
            seg = 'O' * b + '.' * (a - b)
            new_col.append(seg)
        new_col = '#'.join(new_col)
        new_arr.append(list(new_col))
    return new_arr


def go_south(arr) -> list:
    new_arr = []
    for i in range(len(arr[0])):
        col = ''.join([row[i] for row in arr])
        segments = col.split('#')
        new_col = []
        for segment in segments:
            a = len(segment)
            if a == 0:
                new_col.append('')
                continue
            b = segment.count('O')
            seg = '.' * (a - b) + 'O' * b
            new_col.append(seg)
        new_col = '#'.join(new_col)
        new_arr.append(list(new_col))
    return transform_arr(new_arr)


def go_east(arr) -> list:
    new_arr = []
    for row in arr:
        row = ''.join(row)
        segments = row.split('#')
        new_col = []
        for segment in segments:
            a = len(segment)
            if a == 0:
                new_col.append('')
                continue
            b = segment.count('O')
            seg = '.' * (a - b) + 'O' * b
            new_col.append(seg)
        new_col = '#'.join(new_col)
        new_arr.append(list(new_col))
    return new_arr


def cal_dict():
    for key in MY_DICT.keys():
        adders = []
        for i in range(len(MY_DICT[key]) - 1):
            adders.append(MY_DICT[key][i + 1] - MY_DICT[key][i])
        print(key, ' :', MY_DICT[key])





if __name__ == '__main__':
    # fall_rocks('OO.O.O..##')
    main()
    # cal_dict()
    t=0
