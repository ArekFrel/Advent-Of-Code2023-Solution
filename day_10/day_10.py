DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2


class PipeMap:

    def __init__(self):
        self.data = PipeMap.get_map()
        self.first_trip_address = None
        self.first_trip_from = None
        self.second_trip_address = None
        self.second_trip_from = None
        self.start = self.initial_address()
        self.trip_started = False
        self.steps_made = 0
        self.from_directions = []
        self.loop = []
        self.loop_dict = {}
        self.loop_interior = 0

    def pipe_by_address(self, y, x):
        return self.data[y][x]

    @staticmethod
    def get_map():
        data_array = []
        with open(FILE, 'r', encoding='utf-8') as my_input:
            for line in my_input:
                numbers = [x for x in line]
                data_array.append(numbers.copy())
        return data_array

    def go(self):
        if not self.trip_started:
            y, x = self.start
            address_1, address_2 = self.connected_address(y, x)
            self.first_trip_address = address_1
            self.second_trip_address = address_2
            self.trip_started = True
            self.steps_made += 1
            self.loop.append(self.start)
            self.loop.append(address_1)
            self.loop.append(address_2)
            return None

        if self.trip_started:
            y1, x1 = self.first_trip_address
            self.first_trip_address = self.connected_address(y1, x1, self.first_trip_from)
            y2, x2 = self.second_trip_address
            self.second_trip_address = self.connected_address(y2, x2, self.second_trip_from)
            self.second_trip_from = self.from_directions.pop()
            self.first_trip_from = self.from_directions.pop()
            self.loop.append(self.first_trip_address)
            if self.second_trip_address not in self.loop:
                self.loop.append(self.second_trip_address)
            self.steps_made += 1
            return None

    def initial_address(self):
        for i, line in enumerate(self.data):
            if "S" in line:
                return i, self.data[i].index("S")

    def trip(self):
        self.go()
        while self.first_trip_address != self.second_trip_address:
            self.go()

    def connected_address(self, y, x, from_dir=None):
        """this one really needs to be optimized"""
        conneceted_addresses = []
        if self.pipe_by_address(y, x) == "S":
            dir_from = []
            ny, nx = PipeMap.north_neighbour(y, x)
            if self.pipe_by_address(ny, nx) == '|':
                conneceted_addresses.append((ny, nx,))
                dir_from.append('south')
            ny, nx = PipeMap.south_neighbour(y, x)
            if self.pipe_by_address(ny, nx) == '|':
                conneceted_addresses.append((ny, nx,))
                dir_from.append('north')
            ny, nx = PipeMap.west_neighbour(y, x)
            if self.pipe_by_address(ny, nx) == '-':
                conneceted_addresses.append((ny, nx,))
                dir_from.append('east')
            ny, nx = PipeMap.east_neighbour(y, x)
            if self.pipe_by_address(ny, nx) == '-':
                conneceted_addresses.append((ny, nx,))
                dir_from.append('west')
            ny, nx = PipeMap.north_neighbour(y, x)
            if self.pipe_by_address(ny, nx) in ['7', 'F']:
                conneceted_addresses.append((ny, nx,))
                dir_from.append('south')
            ny, nx = PipeMap.east_neighbour(y, x)
            if self.pipe_by_address(ny, nx) in ['J', '7']:
                conneceted_addresses.append((ny, nx))
                dir_from.append('west')
            ny, nx = PipeMap.south_neighbour(y, x)
            if self.pipe_by_address(ny, nx) in ['J', 'L']:
                conneceted_addresses.append((ny, nx))
                dir_from.append('north')
            ny, nx = PipeMap.west_neighbour(y, x)
            if self.pipe_by_address(ny, nx) in ['F', 'L']:
                dir_from.append('east')
                conneceted_addresses.append((ny, nx))
            self.first_trip_from = dir_from[0]
            self.second_trip_from = dir_from[1]
            return conneceted_addresses
        else:
            if self.pipe_by_address(y, x) == "|":
                if from_dir == 'north':
                    self.from_directions.append('north')
                    return PipeMap.south_neighbour(y, x)
                if from_dir == 'south':
                    self.from_directions.append('south')
                    return PipeMap.north_neighbour(y, x)
            if self.pipe_by_address(y, x) == "-":
                if from_dir == 'east':
                    self.from_directions.append('east')
                    return PipeMap.west_neighbour(y, x)
                if from_dir == 'west':
                    self.from_directions.append('west')
                    return PipeMap.east_neighbour(y, x)
            if self.pipe_by_address(y, x) == "L":
                if from_dir == 'east':
                    self.from_directions.append('south')
                    return PipeMap.north_neighbour(y, x)
                if from_dir == 'north':
                    self.from_directions.append('west')
                    return PipeMap.east_neighbour(y, x)
            if self.pipe_by_address(y, x) == "J":
                if from_dir == 'west':
                    self.from_directions.append('south')
                    return PipeMap.north_neighbour(y, x)
                if from_dir == 'north':
                    self.from_directions.append('east')
                    return PipeMap.west_neighbour(y, x)
            if self.pipe_by_address(y, x) == "7":
                if from_dir == 'west':
                    self.from_directions.append('north')
                    return PipeMap.south_neighbour(y, x)
                if from_dir == 'south':
                    self.from_directions.append('east')
                    return PipeMap.west_neighbour(y, x)
            if self.pipe_by_address(y, x) == "F":
                if from_dir == 'east':
                    self.from_directions.append('north')
                    return PipeMap.south_neighbour(y, x)
                if from_dir == 'south':
                    self.from_directions.append('west')
                    return PipeMap.east_neighbour(y, x)

    def loop_calculation(self):
        self.loop.sort(key=lambda x: x[0])
        loop_ys = [y[0] for y in self.loop]
        loop_ys = list(set(loop_ys))
        for key in loop_ys:
            value = [val[1] for val in self.loop if val[0] == key]
            value.sort()
            self.loop_dict[key] = value

    def loop_interior_calculation(self):
        for key in self.loop_dict:
            vals = self.loop_dict[key].copy()
            inside, from_up, from_down = False, False, False
            prev_val = 0
            for val in vals:
                if inside:
                    self.loop_interior += val - prev_val - 1
                    if val - prev_val >= 2:
                        print(f'key:{key} prev:{prev_val} val:{val}')
                value = self.pipe_by_address(key, val)
                if value == "|":
                    inside = not inside
                    from_up, from_down = from_down, from_up
                if value in ['J', 'L']:
                    from_up = not from_up
                elif value in ['F', '7']:
                    from_down = not from_down
                if from_down and from_up:
                    inside = not inside
                    from_up, from_down = False, False
                prev_val = val

    @staticmethod
    def north_neighbour(y, x):
        return y - 1, x

    @staticmethod
    def east_neighbour(y, x):
        return y, x + 1

    @staticmethod
    def south_neighbour(y, x):
        return y + 1, x

    @staticmethod
    def west_neighbour(y, x):
        return y, x - 1


def solve():

    mapa1 = PipeMap()
    mapa1.trip()
    if SOLVE_PART == 1:
        return mapa1.steps_made
    if SOLVE_PART == 2:
        mapa1.loop_calculation()
        mapa1.loop_interior_calculation()
        return mapa1.loop_interior


def main():
    print(f'Result of day {DAY} part {SOLVE_PART} is {solve()}.')


if __name__ == '__main__':
    main()

