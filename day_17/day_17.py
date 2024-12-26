DAY = __file__[-5:-3]
# FILE = f'../inputs/input_{DAY}.txt'
FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1

def formulate_grid():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        return [x.replace('\n', '') for x in my_input.readlines()]

GRID = formulate_grid()

def formulate_score_grid():
    y_len = len(GRID)
    x_len = len(GRID[0])
    score_grid = [[0 for _ in range(x_len)] for _ in range(y_len)]
    return score_grid

SCORE_GRID = formulate_score_grid()



class HeatLoss:

    best_score = None
    steps = []

    CONTINUE_DIR = {'LEFT': 'RIGHT',
              'RIGHT': 'LEFT',
              'UP': 'DOWN',
              'DOWN': 'UP'
              }


    def __init__(self, y_cord, x_cord, dir_from, consecutive, score=0):

        self.y_cord = y_cord
        self.x_cord = x_cord
        self.dir_from = dir_from
        self.consecutive = consecutive
        self.score = score + self.value()


    def next_options(self):
        options_to_go = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        if self.dir_from:
            options_to_go.remove(self.dir_from)
        if self.consecutive == 3:
            options_to_go.remove(self.continue_direction())
        if self.x_cord == 0:
            options_to_go.remove('LEFT')
        if self.x_cord == len(GRID[0]) - 1:
            options_to_go.remove('RIGHT')
        if self.y_cord == 0:
            options_to_go.remove('UP')
        if self.x_cord == len(GRID) - 1:
            options_to_go.remove('DOWN')
        return options_to_go



    def continue_direction(self):
        return HeatLoss.CONTINUE_DIR[self.dir_from]


    def options(self):
        for option in self.next_options():
            self.go(option)






    def value(self):
        return int(GRID[self.y_cord][self.x_cord])

def main():
    heat_loss = HeatLoss(0,0,None,0,0)
    t=0


if __name__ == '__main__':
        main()