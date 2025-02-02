from heapq import heappush, heappop
from copy import deepcopy

DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
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

def read_test_map():
    with open('mapa_test.txt', 'r', encoding='utf-8-sig') as map_input:
        lines = map_input.read().strip().split("\n")
        grid = [line.count('#') for line in lines]

    for i in range(len(grid)):
        if i == 0:
            continue
        grid[i] = grid[i] + grid[i-1]

    return grid


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

    print(f'Result of day {DAY} part {SOLVE_PART} is {result}')


def solve_2():

    test_map = read_test_map()
    temp_x = 0
    temp_y = 0
    point = [0, 0]
    # digged_lines = []
    hor_lines = []
    # ver_lines = []

    for line in DIG_PLAN:
        d, val = line.split(' ')
        val = int(val)
        delta_r, delta_l, delta_d, delta_u = 0, 0, 0, 0
        hor = False
        match d:
            case 'R':
                temp_x += val

                delta_r = val
                hor = True
            case 'L':
                temp_x -= val

                delta_l = val
                hor = True
            case 'D':
                temp_y += val

                delta_d = val
            case 'U':
                temp_y -= val
                delta_u = val
        point_s = point
        point_f = [point_s[0] - delta_u + delta_d, point_s[1] - delta_l + delta_r]
        dig = sorted([point_s[1], point_f[1]])
        rec = (point_s[0], dig)
        if hor:
            assert point_s[0] == point_f[0]
            heappush(hor_lines, rec)

        point = point_f
    hor_lines_list = []
    result = 0
    prev_y_cord = None
    width = 0
    result_tab = []
    min_tab_val = None
    while hor_lines:
        hor_line = heappop(hor_lines)
        y_cord , points = hor_line
        if min_tab_val is None:
            min_tab_val = y_cord
        if prev_y_cord is not None:
            result += width * (y_cord - prev_y_cord - 1)
            result_tab.append([result, y_cord - min_tab_val - 1])
        narrower = 0
        if not hor_lines_list:
            hor_lines_list.append(points)
        else:
            hor_lines_list, reducer = join_width(points, hor_lines_list)
            narrower += reducer
        try:
            while hor_lines[0][0] == y_cord:
                hor_lines_list, reducer = join_width(heappop(hor_lines)[1], hor_lines_list)
                narrower += reducer
        except IndexError:
            pass
        width = calc_width(hor_lines_list)
        prev_y_cord = y_cord
        result += width + narrower
        result_tab.append([result, y_cord - min_tab_val])

    return result


def join_width(dig, lines: list):
    reducer = 0
    if dig in lines:
        lines.remove(dig)
        reducer = dig[1] - dig[0] + 1
        return lines, reducer

    changed = False

    for i in range(len(lines)):
        if i != len(lines) - 1:
            if dig[0] == lines[i][1] and dig[1] == lines[i + 1][0]:
                new_line = [lines[i][0], lines[i + 1][1]]
                lines.remove(lines[i + 1])
                lines.remove(lines[i])
                lines.append(new_line)
                lines.sort()
                changed = True
                break

        if dig[0] == lines[i][0]:
            lines[i] = [dig[1], lines[i][1]]
            reducer = dig[1] - dig[0]
            changed = True
            break
        elif dig[0] == lines[i][1]:
            lines[i] = [lines[i][0], dig[1]]
            changed = True
            break
        elif dig[1] == lines[i][1]:
            lines[i] = [lines[i][0], dig[0]]
            reducer = dig[1] - dig[0]
            changed = True
            break
        elif dig[1] == lines[i][0]:
            lines[i] = [dig[0], lines[i][1]]
            changed = True
            break

        elif lines[i][0] < dig[0] < lines[i][1]:
            lines.append([lines[i][0], dig[0]])
            lines.append([dig[1], lines[i][1]])
            lines.remove(lines[i])
            lines.sort()
            reducer = dig[1] - dig[0] -1
            changed = True
            break


    if not changed:
        lines.append(dig)
        lines.sort()
    return lines, reducer

def calc_width(lines):
    result = 0
    for first, second in lines:
        result += second - first + 1
    return result

if __name__ == '__main__':
    print(f'Result of day {DAY} part {SOLVE_PART} is {solve_2()}')

