import string

DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1

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

    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
        Node.all_nodes[self.name] = self

    def go(self, direction):
        Node.steps_made += 1
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
    print(f'Result of day {DAY} part {SOLVE_PART} is {Node.steps_made}.')


def solve_02():
    pass


def main():

    if SOLVE_PART == 1:
        solve_01()
    if SOLVE_PART == 2:
        solve_02()


if __name__ == '__main__':
    main()
