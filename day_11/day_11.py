import copy
import itertools

DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1


class Universe:

    def __init__(self):
        self.map = Universe.get_map()
        self.galaxies = []
        self.expanded_galaxy = copy.deepcopy(self.map.copy())
        if SOLVE_PART == 1:
            self.expand_galaxy()
        if SOLVE_PART == 2:
            self.old_row_galaxies = self.get_old_row_galaxies()
            self.old_column_galaxies = self.get_old_col_galaxies()
        self.get_galaxies()
        self.galaxies_pairs = self.galaxies_combination()

    @staticmethod
    def get_map():
        data_array = []
        with open(FILE, 'r', encoding='utf-8') as my_input:
            for line in my_input:
                items = [x for x in line if x != '\n']
                data_array.append(items.copy())
        return data_array

    def expand_galaxy(self):
        x_expand = []
        y_expand = []
        for col in range(0, len(self.map[0])):
            column = [x[col] for x in self.map]
            if '#' not in column:
                x_expand.append(col)
        for i, row in enumerate(self.map):
            if '#' not in row:
                y_expand.append(i)

        x_expand.reverse()
        y_expand.reverse()
        for col in x_expand:
            for row in self.expanded_galaxy:
                row.insert(col, '.')
        for row in y_expand:
            self.expanded_galaxy.insert(row, ['.'] * len(self.expanded_galaxy[0]))

    def get_galaxies(self):
        for i, row in enumerate(self.expanded_galaxy):
            for j, col in enumerate(row):
                if col == '#':
                    self.galaxies.append((i, j))

    def get_old_row_galaxies(self):
        rows = []
        for i, row in enumerate(self.map):
            if '#' not in row:
                rows.append(i)
        return set(rows)

    def get_old_col_galaxies(self):
        cols = []
        for col in range(0, len(self.map[0])):
            column = [x[col] for x in self.map]
            if '#' not in column:
                cols.append(col)
        return set(cols)


    def calc_distance(pair):
        def cross_old_row_galaxy(rows, rg):
            i, j = min(rg), max(rg)
            second_set = set(list(range(i,j + 1)))
            return len(rows.intersection(second_set))

        def cross_old_col_galaxy():
            pass


        galaxy_1, galaxy_2 = pair
        i1, j1 = galaxy_1
        i2, j2 = galaxy_2
        return abs(i1 - i2) + abs(j1 - j2) + 1000000 * cross_old_row_galaxy(self.get_old_row_galaxies)

    def galaxies_combination(self):
        return list(itertools.combinations(self.galaxies, 2))

    def calculate_result(self):
        result = 0
        for pair in self.galaxies_pairs:
            result += Universe.calc_distance(pair)
        return result


def solve():

    universe = Universe()

    if SOLVE_PART == 1:
        return universe.calculate_result()
    # if SOLVE_PART == 2:
    #     mapa1.loop_calculation()
    #     mapa1.loop_interior_calculation()
    #     return mapa1.loop_interior


def main():
    print(f'Result of day {DAY} part {SOLVE_PART} is {solve()}.')


if __name__ == '__main__':
    main()

