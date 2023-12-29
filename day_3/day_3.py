FILE = '../inputs/input_03.txt'
# FILE = '../inputs/test_input_03.txt'
DAY = 3
SOLVE_PART = 2
with open(FILE, 'r', encoding='utf-8') as my_input:
    ARRAY = [line for line in my_input]


def solve_part_1():
    array = ARRAY

    def validation_number(rows, columns):
        signs = []
        first_id, last_id = columns
        for row in rows:
            row_slice = list(ARRAY[row][first_id: last_id + 1])
            signs += row_slice
        signs = list(filter(lambda x: not str(x).isdigit() and x != '.' and x != '\n', signs))
        return len(signs) > 0

    validated_numbers = []

    for line_index, line in enumerate(array):
        numbers_in_line = []
        indexes_of_numbers = []
        num = ''
        new_number = True
        for pos, sign in enumerate(line):
            if str(sign).isdigit():
                num = num + sign
                if new_number:
                    new_number = False
                    indexes_of_numbers.append(pos)

            elif num.isdigit():
                numbers_in_line.append(int(num))
                num = ''
                new_number = True
        rows = row_calc(line_index)
        for number in numbers_in_line:
            index = indexes_of_numbers.pop(0)
            columns = column_calc(index, str(number))
            if validation_number(rows, columns):
                validated_numbers.append(number)
    print(sum(validated_numbers), ' numbers by "*"')


def solve_part_2():

    array = ARRAY
    star_cords = []
    validated_numbers = []

    def star_digit_neighbours(cords):
        neighbours = []
        row_cord, col_cord = cords
        rows = row_calc(row_cord)
        columns = column_calc(col_cord)
        for row in rows:
            for column in columns:
                if [row, column] == cords:
                    continue
                if ARRAY[row][column].isdigit():
                    neighbours.append([row, column])
        return neighbours

    def number_by_cords(cords):
        number_array = []
        cord_row, cord_column = cords
        number_array.append(ARRAY[cord_row][cord_column])
        next_col = cord_column + 1
        while next_col <= len(ARRAY) - 1 and ARRAY[cord_row][next_col].isdigit() :
            number_array.append(ARRAY[cord_row][next_col])
            next_col += 1
        prev_col = cord_column - 1
        while prev_col >= 0 and ARRAY[cord_row][prev_col].isdigit():
            number_array.insert(0, ARRAY[cord_row][prev_col])
            prev_col -= 1
        num = int(''.join(number_array))
        return [num, cord_row, [prev_col + 1, next_col - 1]]
        
    for line_index, line in enumerate(array):
        for sign_index, sign in enumerate(line):
            if sign == "*":
                star_cords.append([line_index, sign_index])

    for star in star_cords:
        stars_neighbours = star_digit_neighbours(star)
        if len(stars_neighbours) > 1:
            numbers = []
            for neighbour in stars_neighbours:
                num = number_by_cords(neighbour)
                if num not in numbers:
                    numbers.append(num)
            if len(numbers) == 2:
                validated_numbers.append(numbers[0][0] * numbers[1][0])

    print(f'Result of day {DAY} part {SOLVE_PART} is {sum(validated_numbers)}.')


def row_calc(row):
    no_of_rows = len(ARRAY)
    first_row = row - 1 if row > 0 else None
    last_row = row + 1 if row + 1 < no_of_rows else None
    rows = list(filter(lambda x: isinstance(x, int), [first_row, row, last_row]))
    return rows


def column_calc(column, number='*'):
    no_of_columns = len(ARRAY[0])
    num_len = len(str(number))
    first_column = column - 1 if column > 0 else column
    last_column = column + num_len if column + num_len <= no_of_columns else column + num_len -1
    columns = list(filter(lambda x: isinstance(x, int), [first_column, column, last_column]))
    if SOLVE_PART == 1:
        return min(columns), max(columns)
    if SOLVE_PART == 2:
        return columns


def main():
    if SOLVE_PART == 1:
        solve_part_1()
    if SOLVE_PART == 2:
        solve_part_2()


if __name__ == '__main__':
    main()


