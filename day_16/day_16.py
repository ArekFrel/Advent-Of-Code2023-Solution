DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2


def formulate_grid():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        return [x[:-1] for x in my_input.readlines()]


class Beam:
    GRID =  formulate_grid()

    def __init__(self, direction, cord_y, cord_x):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.direction = direction

    def go(self):
        meets = Beam.GRID[self.cord_y, self.cord_x]

        if meets == '.':
            if self.direction == "RIGHT" :
                self.cord_x += 1
                return
            if self.direction == "LEFT":
                self.cord_x -= 1
                return
            if self.direction == "UP":
                self.cord_y += 1
                return
            if self.direction == "DOWN":
                self.cord_y -= 1
                return

        if meets == '\\':
            if self.direction == "RIGHT":
                self.cord_y -= 1
                self.direction = 'DOWN'
                return
            if self.direction == "LEFT":
                self.cord_y += 1
                self.direction = 'UP'
                return
            if self.direction == "UP":
                self.cord_x -= 1
                self.direction = 'LEFT'
                return
            if self.direction == "DOWN":
                self.cord_x += 1
                self.direction = 'RIGHT'
                return

        if meets == '/':
            if self.direction == "RIGHT":
                self.cord_y += 1
                self.direction = 'UP'
                return
            if self.direction == "LEFT":
                self.cord_y -= 1
                self.direction = 'DOWN'
                return
            if self.direction == "UP":
                self.cord_x += 1
                self.direction = 'RIGHT'
                return
            if self.direction == "DOWN":
                self.cord_x -= 1
                self.direction = 'LEFT'
                return

        if meets == '|':
            if self.direction == "RIGHT":
                self.cord_y += 1
                self.direction = 'UP'
                return
            if self.direction == "LEFT":
                self.cord_y -= 1
                self.direction = 'DOWN'
                return
            if self.direction == "UP":
                self.cord_x += 1
                self.direction = 'RIGHT'
                return
            if self.direction == "DOWN":
                self.cord_x -= 1
                self.direction = 'LEFT'
                return






def main():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        grid = [x[:-1] for x in my_input.readlines()]
        a=0


if __name__ == '__main__':
    main()
