import sys

sys.setrecursionlimit(4000)

DAY = __file__[-5:-3]
# FILE = f'../inputs/input_{DAY}.txt'
FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1


def formulate_grid():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        return [x.replace('\n', '') for x in my_input.readlines()]

GRID = formulate_grid()

class Beam:

    split_beams = []
    cords_met = []
    situations = []
    best_score = 0
    went = 0

    def __init__(self, direction, cord_y, cord_x, do_clear=False):
        if do_clear:
            Beam.clear_data()
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.direction = direction
        self.go()
        if do_clear:
            if len(Beam.cords_met) > Beam.best_score:
                Beam.best_score = len(Beam.cords_met)

    @staticmethod
    def clear_data():
        Beam.cords_met.clear()
        Beam.situations.clear()
        Beam.split_beams.clear()

    def go(self):
        if any((self.cord_x < 0, self.cord_y < 0)):
            return None
        try:
            meets = GRID[self.cord_y][self.cord_x]
        except IndexError:
            return None
        if (self.cord_y, self.cord_x) not in Beam.cords_met:
            Beam.cords_met.append((self.cord_y, self.cord_x))
        if (self.cord_y, self.cord_x, self.direction) not in Beam.situations:
            Beam.situations.append((self.cord_y, self.cord_x, self.direction))
        else:
            return None


        match meets:
            case '.':
                match self.direction:
                    case "RIGHT":
                        self.cord_x += 1
                    case "LEFT":
                        self.cord_x -= 1
                    case "UP":
                        self.cord_y -= 1
                    case "DOWN":
                        self.cord_y += 1

            case '\\':
                match self.direction:
                    case "RIGHT":
                        self.cord_y += 1
                        self.direction = 'DOWN'
                    case "LEFT":
                        self.cord_y -= 1
                        self.direction = 'UP'
                    case "UP":
                        self.cord_x -= 1
                        self.direction = 'LEFT'
                    case "DOWN":
                        self.cord_x += 1
                        self.direction = 'RIGHT'

            case '/':
                    match self.direction:
                        case "RIGHT":
                            self.cord_y -= 1
                            self.direction = 'UP'
                        case "LEFT":
                            self.cord_y += 1
                            self.direction = 'DOWN'
                        case "UP":
                            self.cord_x += 1
                            self.direction = 'RIGHT'
                        case "DOWN":
                            self.cord_x -= 1
                            self.direction = 'LEFT'

            case '|':
                match self.direction:
                    case "RIGHT":
                        Beam.split_beams.append(Beam(direction='UP', cord_x=self.cord_x, cord_y=self.cord_y-1))
                        Beam.split_beams.append(Beam(direction='DOWN', cord_x=self.cord_x, cord_y=self.cord_y+1))
                        return None
                    case "LEFT":
                        Beam.split_beams.append(Beam(direction='UP', cord_x=self.cord_x, cord_y=self.cord_y-1))
                        Beam.split_beams.append(Beam(direction='DOWN', cord_x=self.cord_x, cord_y=self.cord_y+1))
                        return None

                    case "UP":
                        self.cord_y -= 1
                    case "DOWN":
                        self.cord_y += 1

            case '-':
                match self.direction:
                    case "RIGHT":
                        self.cord_x += 1
                    case "LEFT":
                        self.cord_x -= 1
                    case "UP":
                        self.split_beams.append(Beam(direction='LEFT', cord_x=self.cord_x-1, cord_y=self.cord_y))
                        self.split_beams.append(Beam(direction='RIGHT', cord_x=self.cord_x+1, cord_y=self.cord_y))
                        return None
                    case "DOWN":
                        self.split_beams.append(Beam(direction='LEFT', cord_x=self.cord_x-1, cord_y=self.cord_y))
                        self.split_beams.append(Beam(direction='RIGHT', cord_x=self.cord_x+1, cord_y=self.cord_y))
                        return None
        # try:
        self.go()
        # except RecursionError:
        #     t = 0

def main():

    if SOLVE_PART == 1:
        # Beam(direction='RIGHT', cord_x=0, cord_y=0, do_clear=True)
        beam = Beam(direction='RIGHT', cord_x=0, cord_y=0, do_clear=True)
        a = 0

    if SOLVE_PART == 2:
        x_len = len(GRID[0])
        y_len = len(GRID)
        for x in range(x_len):
            Beam(direction='DOWN', cord_x=x, cord_y=0, do_clear=True)
            print(f'{x=} y =0  score = {len(Beam.cords_met)}')
            Beam(direction='UP', cord_x=x, cord_y=y_len-1, do_clear=True)
            print(f'{x=} y ={y_len-1}  score = {len(Beam.cords_met)}')
        for y in range(y_len):
            Beam(direction='RIGHT', cord_x=0, cord_y=y, do_clear=True)
            print(f'x=0 y ={y}    score = {len(Beam.cords_met)}')
            Beam(direction='LEFT', cord_x=x_len-1, cord_y=y, do_clear=True)
            print(f'x={x_len-1} y ={y}    score = {len(Beam.cords_met)}')


    print(f'Result of day{DAY} part {SOLVE_PART} is {Beam.best_score}')




if __name__ == '__main__':
    main()
