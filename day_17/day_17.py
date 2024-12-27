import sys
from heapq import heappush, heappop
DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2

def formulate_grid():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        lines = my_input.read().strip().split("\n")
        return [[int(_) for _ in line] for line in lines]

GRID = formulate_grid()
Y = len(GRID)
X = len(GRID[0])

def solve():

    dirs = [(0, 1) ,(-1, 0) ,(0, -1) ,(1, 0)]
    pq = [(0, (0,0), None, 0)]
    been_here = set()
    result = 0

    #returns reverse direction
    dir_dict = {
        0: 2,
        1: 3,
        2: 0,
        3: 1
    }

    while pq:
        score, loc, d, steps = heappop(pq)
        # score is heatloss so far
        # loc is (i,j) location
        # d is direction recently went
        # steps - number of steps in given direction
        if (loc, d, steps) in been_here:
            continue
        been_here.add((loc, d, steps))

        if SOLVE_PART == 1 and loc == (Y - 1, X - 1):
            result = score
            break
        if SOLVE_PART == 2 and loc == (Y - 1, X - 1) and steps >= 4:
            result = score
            break

        y, x = loc
        for new_dir in range(4):
            if SOLVE_PART == 1:
                if d is not None:
                    if steps >= 3 and new_dir == d:
                        continue
                    if new_dir == dir_dict[d]:
                        continue

                dy, dx = dirs[new_dir]
                yy = y + dy
                xx = x + dx
                if not (0 <= yy < Y and 0 <= xx < X):
                    continue
                if new_dir == d:
                    assert steps < 3
                    new_steps = steps + 1
                else:
                    new_steps = 1
                new_score = score + GRID[yy][xx]

            if SOLVE_PART == 2:
                if d is not None:
                    if steps < 4 and new_dir != d:
                        continue
                    if steps == 10 and new_dir == d:
                        continue
                    if new_dir == dir_dict[d]:
                        continue

                dy, dx = dirs[new_dir]
                yy = y + dy
                xx = x + dx
                if not (0 <= yy < Y and 0 <= xx < X):
                    continue
                if new_dir == d:
                    assert steps <= 10
                    new_steps = steps + 1
                else:
                    new_steps = 1
                    if d is not None:
                        assert steps >= 4
                new_score = score + GRID[yy][xx]

            heappush(pq, (new_score, (yy, xx), new_dir, new_steps))

    return result

def solve_2():

    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    pq = [(0, (0, 0), None, 0)]
    been_here = set()
    result = 0

    # returns reverse direction
    dir_dict = {
        0: 2,
        1: 3,
        2: 0,
        3: 1
    }

    while pq:
        score, loc, d, steps = heappop(pq)
        # score is heatloss so far
        # loc is (i,j) location
        # d is direction recently went
        # steps - number of steps in given direction
        if (loc, d, steps) in been_here:
            continue
        been_here.add((loc, d, steps))

        if loc == (Y - 1, X - 1) and steps >= 4:
            result = score
            break

        y, x = loc
        for new_dir in range(4):
            if d is not None:
                if steps < 4 and new_dir != d:
                    continue
                if steps == 10 and new_dir == d:
                    continue
                if new_dir == dir_dict[d]:
                    continue

            dy, dx = dirs[new_dir]
            yy = y + dy
            xx = x + dx
            if not (0 <= yy < Y and 0 <= xx < X):
                continue
            if new_dir == d:
                assert steps <= 10
                new_steps = steps + 1
            else:
                new_steps = 1
                if d is not None:
                    assert steps >= 4

            new_score = score + GRID[yy][xx]

            heappush(pq, (new_score, (yy, xx), new_dir, new_steps))
    return result

def main():
    print(f'Result of day {DAY} part {SOLVE_PART} is {solve()}')


if __name__ == '__main__':
        main()