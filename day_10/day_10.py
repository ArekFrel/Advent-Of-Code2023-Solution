from math import prod
DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1


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
            return None

        if self.trip_started:
            y1, x1 = self.first_trip_address
            self.first_trip_address = self.connected_address(y1, x1, self.first_trip_from)
            y2, x2 = self.second_trip_address
            self.second_trip_address = self.connected_address(y2, x2, self.second_trip_from)
            self.second_trip_from = self.from_directions.pop()
            self.first_trip_from = self.from_directions.pop()
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
    return mapa1.steps_made


def main():
    print(f'Result of day {DAY} part {SOLVE_PART} is {solve()}.')


if __name__ == '__main__':
    main()

