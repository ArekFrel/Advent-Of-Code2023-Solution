DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2
# MY_DICT = []

class Box:

    def __init__(self):
        self.box = []

    def search_label(self, label):
        for i in range(len(self.box)):
            if self.box[i].label == label:
                return i
        return False

    def del_label(self, label:str):
        for i in range(len(self.box)):
            if self.box[i].label == label:
                self.box.pop(i)
                break

    def add_len(self, lens):

        for i in range(len(self.box)):
            if self.box[i].label == lens.label:
                self.box[i].focal = lens.focal
                return True
        self.box.append(lens)

    def calculate_power(self, j):
        result = 0
        for i, lens in enumerate(self.box, 1):
            result += j * i * lens.focal
        return result




class Lens:

    def __init__(self, label, focal):
        self.label = label
        self.focal = focal


def main():

    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        line = my_input.readline()
        codes = line.split(',')
        if SOLVE_PART == 1:
            big_results = []
            for code in codes:
                big_results.append(hash_algorithm(code))
            print(f'The Result of part {SOLVE_PART} is {sum(big_results)}')
        if SOLVE_PART == 2:
            boxes = [Box() for _ in range(256)]
            for code in codes:
                box_id, label, operator, focal = unpack_code(code)
                if operator == '-':
                    boxes[box_id].del_label(label=label)
                if operator == '=':
                    boxes[box_id].add_len(Lens(label, focal))
            result = 0
            for j, box in enumerate(boxes, 1):
                result += box.calculate_power(j)
            print(f'The Result of part {SOLVE_PART} is {result}')


def unpack_code(code:str) -> (str, str, int):

    if '=' in code:
        op_id = code.index('=')
        label = code[:op_id]
        box_id = hash_algorithm(label)
        focal = int(code[op_id + 1:])
        return box_id, label, '=',focal

    if '-' in code:
        label = code[0: -1]
        box_id = hash_algorithm(label)
        return box_id, label, '-',None


def hash_algorithm(code:str) -> int:
    result = 0
    for sign in code:
        x = ord(sign) + result
        result = (17 * x) % 256
    return result



if __name__ == '__main__':

    main()

