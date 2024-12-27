import sys
from heapq import heappush, heappop
from copy import deepcopy
DAY = __file__[-5:-3]
# FILE = f'../inputs/input_{DAY}.txt'
FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2

DIR_DICT = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

def formulate_grid():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        lines = my_input.read().strip().split("\n")
        return [line.split(' (')[0] for line in lines]

def formulate_grid_hex():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        lines = my_input.read().strip().split("\n")
        grid = [line.split(' (#')[1][0:-1] for line in lines]

    new_grid = []
    for line in grid:
        code, d = line[0:-1], line[-1]
        new_line = f'{DIR_DICT[d]} {int(code, 16)}'
        new_grid.append(new_line)

    return new_grid
if SOLVE_PART == 1:
    DIG_PLAN = formulate_grid()
else:
    DIG_PLAN = formulate_grid_hex()

EMPTY_SIGN = '.'
DIGGED_SIGN = '#'

# drawing an empty map of proper size
def create_map  (y, x):
    return [[EMPTY_SIGN for _ in range(x)] for _ in range(y)]


def solve_1():

    max_x, max_xl, max_xr = 0, 0, 0 # size of the digging map along horizontal axis
    max_y, max_yu, max_yd = 0, 0, 0  # size of the digging map along vertical axis
    temp_x = 0
    temp_y = 0
    for line in DIG_PLAN:
        d, val = line.split(' ')
        val = int(val)
        match d:
            case 'R':
                temp_x += val
                if temp_x > max_xr:
                    max_xr = temp_x
            case 'L':
                temp_x -= val
                if temp_x < max_xl:
                    max_xl = temp_x

            case 'D':
                temp_y += val
                if temp_y > max_yd:
                    max_yd = temp_y
            case 'U':
                temp_y -= val
                if temp_y < max_yu:
                    max_yu = temp_y


    max_x = max_xr - max_xl + 1
    max_y = max_yd - max_yu + 1
    # size of the map just has been calculated
    dig_map = create_map(max_y, max_x)

    point = [abs(max_yu), abs(max_xl)]
    yy, xx = point
    dig_map[yy][xx] = DIGGED_SIGN

    # drawing a border of digging below:
    for line in DIG_PLAN:
        d, val = line.split(' ')
        val = int(val)
        match d:
            case 'R':
                delta_y = 0
                delta_x = 1
            case 'L':
                delta_y = 0
                delta_x = -1
            case 'D':
                delta_y = 1
                delta_x = 0
            case 'U':
                delta_y = -1
                delta_x = 0

        for step in range(val):
            y, x = point
            point = [y + delta_y, x + delta_x]
            new_y, new_x = point
            dig_map[new_y][new_x] = DIGGED_SIGN
    filled_map = deepcopy(dig_map)

    # filling interior of the map
    for i, y_line in enumerate(dig_map):
        if i in (0, max_y - 1):
            continue
        # cb - crossed border
        # cu - border came from up
        # cd - border came from down
        # inside - location inside loop

        cu, cd, inside = False, False, False

        if i == 5:
            pass
        for j in range(max_x):


            if dig_map[i][j] == EMPTY_SIGN and not inside:
                continue

            if dig_map[i][j] == EMPTY_SIGN and inside:
                filled_map[i][j] = DIGGED_SIGN
                continue

            if dig_map[i][j] == DIGGED_SIGN and not any([cu, cd]):
                cu = dig_map[i - 1][j] == DIGGED_SIGN
                cd = dig_map[i + 1][j] == DIGGED_SIGN
                if cu and cd:
                    inside = not inside
                    cu, cd = False, False
                continue

            if dig_map[i][j] == DIGGED_SIGN and any([cu, cd]):
                prev_cu, prev_cd = cu, cd
                cu = dig_map[i - 1][j] == DIGGED_SIGN
                cd = dig_map[i + 1][j] == DIGGED_SIGN

                if not any([cu, cd]):
                    cu, cd = prev_cu, prev_cd
                    continue

                for curr, prev in [[cd, prev_cd], [cu, prev_cu]]:
                    if curr and prev:
                        cd, cu = False, False
                        continue

                for curr, prev in [[cd, prev_cu], [cu, prev_cd]]:
                    if curr and prev:
                        inside = not inside
                        cd, cu = False, False
    result = 0
    for line in filled_map:
        result += line.count(DIGGED_SIGN)

    # for x in filled_map:
    #     print(''.join(x))
    # print(f'Result of day {DAY} part {SOLVE_PART} is {result}')
    #
    # print(349 * '-')
    #
    # for x in dig_map:
    #     print(''.join(x))
    print(f'Result of day {DAY} part {SOLVE_PART} is {result}')


if __name__ == '__main__':
    solve_1()


