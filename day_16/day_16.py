import sys

sys.setrecursionlimit(3000)

DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2


class Beam:

    @staticmethod
    def formulate_grid():
        with open(FILE, 'r', encoding='utf-8-sig') as my_input:
            return [x[:-1] for x in my_input.readlines()]

    grid = formulate_grid()
    cords_met = []
    situations = []
    went = 0

    def __init__(self, direction, cord_y, cord_x):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.direction = direction
        self.split_beams = []
        self.go()


    def go(self):
        if any((self.cord_x < 0, self.cord_y < 0)):
            return None
        try:
            meets = Beam.grid[self.cord_y][self.cord_x]
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
                        self.split_beams.append(Beam(direction='UP', cord_x=self.cord_x, cord_y=self.cord_y-1))
                        self.split_beams.append(Beam(direction='DOWN', cord_x=self.cord_x, cord_y=self.cord_y+1))
                        return None
                    case "LEFT":
                        self.split_beams.append(Beam(direction='UP', cord_x=self.cord_x, cord_y=self.cord_y-1))
                        self.split_beams.append(Beam(direction='DOWN', cord_x=self.cord_x, cord_y=self.cord_y+1))
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
    # with open(FILE, 'r', encoding='utf-8-sig') as my_input:
    #     grid = [x[:-1] for x in my_input.readlines()]
    #     a=0
    beam = Beam(direction='RIGHT', cord_x=0, cord_y=0)

    print(f'Result of day{DAY} part {SOLVE_PART} is {len(beam.cords_met)}')




if __name__ == '__main__':
    main()
