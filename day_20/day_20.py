import math
DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2

class Module:

    hpc = 0 #high pulse counter
    lpc = 0 #low pulse counter
    pulse_counter = 0
    queue = [] # (from, to, pulse)
    modules_dict = {}
    rx_grand_feeder_dict = {}

    def __init__(self, name, kind, dest_modules):
        self.name = name
        self.kind = kind
        self.dest_modules = dest_modules
        if self.kind == '%':
            self.state = False # False is OFF, True is ON
        if self.kind =='&':
            self.memory = {}
        Module.modules_dict[self.name] = self

    def __repr__(self):
        return f'{self.kind} {self.name}'

    def operate_pulse(self, received_pulse=0, mod_from=None):
        # 1 - high pulse, 0 - low pulse

        match self.kind:

            case 'broadcaster':
                pulse_type = received_pulse

            case '%':
                if received_pulse == 1:
                    return
                if received_pulse == 0:
                    if not self.state:
                        pulse_type = 1
                    if self.state:
                        pulse_type = 0
                    self.state = not self.state

            case '&':
                self.memory[mod_from] = received_pulse
                if not any([val == 0 for val in self.memory.values()]):
                    pulse_type = 0
                else:
                    pulse_type = 1

        assert pulse_type is not None
        for dest in self.dest_modules:
            Module.queue.append((self.name, pulse_type, dest))


    @staticmethod
    def fly_pulse(button_pressed):
        while Module.queue:
            start, pulse_type, dest = Module.queue.pop(0)
            if pulse_type:
                Module.hpc += 1
            else:
                Module.lpc += 1
            # print(f'{start} {pulse_type} -> {dest}')
            module = Module.modules_dict.get(dest)
            if not module:
                continue
            if SOLVE_PART == 2:
                if start in Module.rx_grand_feeder_dict.keys() and pulse_type:
                    if Module.rx_grand_feeder_dict[start] == 0:
                        Module.rx_grand_feeder_dict[start] = button_pressed

            module.operate_pulse(pulse_type, start)

    @staticmethod
    def push_the_button():
        button_pressed = 0
        if SOLVE_PART == 1:
            for i in range(1000):
                # print(f'button 0 -> broadcaster')
                button_pressed += 1
                Module.lpc += 1
                broadcaster = Module.modules_dict['broadcaster']
                broadcaster.operate_pulse()
                Module.fly_pulse(button_pressed)

            print(f'{button_pressed=}')
            print(f'{Module.hpc=} {Module.lpc=}')
            print(f'Result is {Module.hpc * Module.lpc}')

        if SOLVE_PART == 2:
            while any(x == 0 for x in Module.rx_grand_feeder_dict.values()):
                button_pressed += 1
                # Module.lpc += 1
                broadcaster = Module.modules_dict['broadcaster']
                broadcaster.operate_pulse()
                # if button_pressed % 100 == 0:
                #     print(Module.modules_dict['vr'].memory)
                Module.fly_pulse(button_pressed)

            print(f'Result is {math.prod(Module.rx_grand_feeder_dict.values())}')
            print(Module.rx_grand_feeder_dict)


def main():
    inputs_dict = {}

    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        for line in my_input:
            module, destination = line.split('->')
            module = module.rstrip()
            if not module.startswith('broadcaster'):
                module_name = module[1:]
                module_type = module[0]
            else:
                module_name = module
                module_type = module
            destination = destination.rstrip()
            if ',' in destination:
                destination = destination.split(',')
            else:
                destination = [destination]
            destination = list(map(lambda x: x.strip(), destination))
            Module(module_name, module_type, destination)
            if module == 'broadcaster':
                continue
            for module in destination :
                module = module.strip()
                if module not in inputs_dict.keys():
                    inputs_dict[module] = [module_name]
                else:
                    inputs_dict[module].append(module_name)

    for key, values in inputs_dict.items():
        module = Module.modules_dict.get(key)
        if not module:
            continue
        if module and module.kind == '&':
            for value in values:
                module.memory[value] = 0
    # for part II
    rx_feeder = inputs_dict['rx']
    for feeder in rx_feeder:
        for mod in Module.modules_dict[feeder].memory.keys():
            Module.rx_grand_feeder_dict[mod] = 0
    Module.push_the_button()



if __name__ == '__main__':
    main()








