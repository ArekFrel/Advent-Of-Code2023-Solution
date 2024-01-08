from math import prod
from helper import get_n_primes, is_prime
DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2
PRIMAL_NUMBERS = get_n_primes(2000)


class Path:

    def __init__(self, path):
        self.path = path
        self.current_step = -1

    def next_step(self):
        if self.current_step == len(self.path) - 1:
            self.current_step = 0
            return self.direction_by_step()
        else:
            self.current_step += 1
            return self.direction_by_step()

    def direction_by_step(self):
        return self.path[self.current_step]


class Node:
    all_nodes = {}
    steps_made = 0
    steps_made_list = []

    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
        Node.all_nodes[self.name] = self

    def go(self, direction):
        if direction == 'L':
            return Node.node_by_name(self.left)
        else:
            return Node.node_by_name(self.right)

    @staticmethod
    def node_by_name(name):
        return Node.all_nodes.get(name)


def get_path():
    with open(FILE, 'r', encoding='utf-8') as my_input:
        path_to_follow = my_input.readline().rstrip()
    return path_to_follow


def get_nodes():
    with open(FILE, 'r', encoding='utf-8') as my_input:
        for i, line in enumerate(my_input):
            if i < 2:
                continue
            node_name = line[0: line.index(' =')]
            left = line[line.index('(') + 1: line.index(',')]
            right = line[line.index(', ') + 2: line.index(')')]
            new_node = Node(node_name, left, right)
    return new_node


def check_z(array):
    for _ in array:
        if _[2] != "Z":
            return False
    return True


def get_factors(num):

    factors = []
    while not is_prime(num):
        for number in PRIMAL_NUMBERS:
            if num % number == 0:
                factors.append(number)
                num = num / number
                break
    factors.append(num)
    return factors


def lcm(numbers):

    """ Returm less commom multiple"""
    factors = []
    for number in numbers:
        factors += get_factors(number)
    set_of_factors = set(factors)
    factors = list(set_of_factors)
    lcm = prod(factors)
    return int(lcm)


def solve_01():

    path = Path(get_path())
    get_nodes()
    start_node = 'AAA'
    dest_node = 'ZZZ'
    node_name = start_node
    while node_name != dest_node:
        node = Node.node_by_name(node_name)
        direction = path.next_step()
        next_node = node.go(direction)
        node_name = next_node.name
        Node.steps_made += 1
    print(f'Result of day {DAY} part {SOLVE_PART} is {Node.steps_made}.')


def solve_02():
    path = Path(get_path())
    get_nodes()
    all_nodes = list(Node.all_nodes.keys())
    a_start_nodes = list(filter(lambda x: x[2] == "A", all_nodes))

    ''' Checking when all steps get to "**Z" in one time may be time consuming...
    let's check how many steps it got to be taken for each "**A" until it get "**Z"
    After that lets calculate LCM for those number of steps, and here we go...'''
    for node in a_start_nodes:
        node_name = node
        while node_name[2] != 'Z':
            node = Node.node_by_name(node_name)
            direction = path.next_step()
            next_node = node.go(direction)
            node_name = next_node.name
            Node.steps_made += 1
        Node.steps_made_list.append(Node.steps_made)
        Node.steps_made = 0
        path.current_step = -1

    print(f'Result of day {DAY} part {SOLVE_PART} is {lcm(Node.steps_made_list)}.')



def main():

    if SOLVE_PART == 1:
        solve_01()
    if SOLVE_PART == 2:
        solve_02()


if __name__ == '__main__':
    main()
