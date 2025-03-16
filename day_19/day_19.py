DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2


def divide_range(rg: range, num: int):
    if num in rg:
        return range(rg.start, num), range(num, rg.stop)
    else:
        return rg, rg

class Part:

    PARTS = []

    def __init__(self, text):
        vals = text.split(',')
        self.x = int(vals[0][3:])
        self.m = int(vals[1][2:])
        self.a = int(vals[2][2:])
        self.s = int(vals[3].rstrip()[2:-1])
        self.rules = []
        Part.PARTS.append(self)

    def __str__(self):
        return f'{self.x=}, {self.m=}, {self.a=}, {self.s=}'

    def __getitem__(self, item):
        match item:
            case 'x':
                return self.x
        match item:
            case 'm':
                return self.m
        match item:
            case 'a':
                return self.a
        match item:
            case 's':
                return self.s


    def val(self):
        return self.x + self.m + self.a + self.s

    @staticmethod
    def calc_val():
        r = 0
        for x in Part.PARTS:
            if x.s > 2529:
                r += 1
        return r


class PartCalc:

    parts = []
    accepted = 0

    def __init__(self, rx:range, rm:range, ra:range, rs:range, rule):
        self.rx = rx
        self.rm = rm
        self.ra = ra
        self.rs = rs
        self.rule = rule
        PartCalc.parts.append(self)

    def __getitem__(self, item):
        match item:
            case 'x':
                return self.rx
        match item:
            case 'm':
                return self.rm
        match item:
            case 'a':
                return self.ra
        match item:
            case 's':
                return self.rs

    def __repr__(self):
        return self.rule

    def divide(self, category, num, bigger, new_wrkfl):
        dx, dm, da, ds = 0, 0, 0, 0
        match category:
            case 'x':
                dx = num
            case 'm':
                dm = num
            case 'a':
                da = num
            case 's':
                ds = num

        nrx = divide_range(self.rx, dx)
        nrm = divide_range(self.rm, dm)
        nra = divide_range(self.ra, da)
        nrs = divide_range(self.rs, ds)
        if bigger:
            i, j = 0, 1
        else:
            i, j = 1, 0

        PartCalc(nrx[j], nrm[j], nra[j], nrs[j], new_wrkfl)
        self.rx = nrx[i]
        self.rm = nrm[i]
        self.ra = nra[i]
        self.rs = nrs[i]

    def quantity(self):
        return len(self.rx) * len(self.rm) * len(self.ra) * len(self.rs)

    def process_rule(self):
        if self.rule == 'R':
            return
        if self.rule == 'A':
            PartCalc.accepted += self.quantity()
            return
        workflow = Rule.RULES[self.rule]
        for rule in workflow.set_of_rules:
            # if rule == 'A':
            #     PartCalc.accepted += self.quantity()
            #     return
            # if rule == 'R':
            #     return
            if '>' not in rule and '<' not in rule:
                new_wrkfl = rule
                new_part = PartCalc(
                    self.rx,
                    self.rm,
                    self.ra,
                    self.rs,
                    new_wrkfl
                )
                return

            category = rule[0]
            bigger = rule[1] == '>'
            num = int(rule[2:rule.index(':')])
            if rule[1] == '>':
                num += 1
            new_wrkfl = rule[rule.index(':') + 1:]
            if num in self[category]:
                self.divide(category, num, bigger, new_wrkfl)

class Rule:

    RULES = {}
    PARTS_RESULT = 0
    rules_taken = 0

    def __init__(self, text):
        self.name = text[0:text.index('{')]
        self.set_of_rules = text[text.index('{') + 1 : - 2].rstrip().split(',')
        Rule.RULES[self.name] = self

    def __str__(self):
         return self.name + '= ' + ' '.join(self.set_of_rules)

    def __repr__(self):
        return '=' + self.name + '= ' + ' '.join(self.set_of_rules)


    def process_rules(self, part: Part):
        part.rules.append(self.name)
        for rule in self.set_of_rules:
            if rule == 'R':
                part.rules.append('R')
                print(f'REJECTED {part} {' '.join(part.rules)}')
                return
            if rule == 'A':
                Rule.PARTS_RESULT += part.val()
                part.rules.append('A')
                print(f'accepted {part} {' '.join(part.rules)}')
                return
            if '>' not in rule and '<' not in rule:
                new_rule = Rule.RULES[rule.rstrip()]
                # print(f'just go to rule {new_rule.name} ')
                new_rule.process_rules(part)
                return
            category = rule[0]
            # compare = rule[1] == '>'
            if rule[1] == '>':
                compare = int.__gt__
            else:
                compare = int.__lt__
            num = int(rule[2:rule.index(':')])
            go_to_rule = rule[rule.index(':') + 1:]
            if not compare(part[category], num):
                continue
            # match bigger:
            #     case True:
            #         if part[category] <= num:
            #             # print(f'{part[category]} < {num}')
            #             continue
            #     case False:
            #         if part[category] >= num:
            #             # print(f'{part[category]} > {num}')
            #             continue
            if go_to_rule == 'R':
                part.rules.append('R')
                print(f'REJECTED {part} {' '.join(part.rules)}')
                return
            if go_to_rule == 'A':
                Rule.PARTS_RESULT += part.val()
                part.rules.append('A')
                print(f'accepted {part} {' '.join(part.rules)}')
                return
            new_rule = Rule.RULES[go_to_rule]
            new_rule.process_rules(part)
            return

'''Below function was rewritten from youtuber to verify where I was mistaken...'''
def comparing():

    ops = {
        ">": int.__gt__,
        "<": int.__lt__
    }

    def accept(item, name='in'):
        if name == 'R':
            print(f'REJECTED')
            return False
        if name == 'A':
            print(f'Aacepted')
            return True

        rules, fallback = workflows[name]
        for key, cmp, n, target in rules:
            if ops[cmp](item[key], n):
                return accept(item, target)
        return accept(item, fallback)

    workflows = {}
    block_1, block_2 = open(FILE).read().split('\n\n')

    for line in block_1.splitlines():
        name, rest = line[:-1].split('{')
        rules = rest.split(',')
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(':')
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))
    total = 0
    for line in block_2.splitlines():
        item = {}
        for segment in line[1:-1].split(","):
            ch, n = segment.split('=')
            item[ch] = int(n)
        if accept(item):
            total += sum(item.values())
    print(total)


def main():
    if SOLVE_PART == 1:
        with open(FILE, 'r', encoding='utf-8-sig') as my_input:
            lines = my_input.readlines()
            rules_done = False
            for line in lines:
                if line == '\n':
                    rules_done = True
                    continue
                if not rules_done:
                    Rule(line)
                    continue
                else:
                    part = Part(line)
                    start_rule = Rule.RULES['in']
                    start_rule.process_rules(part)
        print(Rule.PARTS_RESULT)
    if SOLVE_PART == 2:
        with open(FILE, 'r', encoding='utf-8-sig') as my_input:
            for line in my_input:
                if line == '\n':
                    break
                a = Rule(line)
        part_calc = PartCalc(range(1,4001), range(1,4001), range(1,4001), range(1,4001), 'in')
        while PartCalc.parts:
            p = PartCalc.parts.pop()
            p.process_rule()
        print(PartCalc.accepted)


if __name__ == '__main__':
    # comparing()
    main()












