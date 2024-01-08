from math import prod
DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1


def get_numbers():
    data_array = []
    with open(FILE, 'r', encoding='utf-8') as my_input:
        for line in my_input:
            numbers = [int(x) for x in line.split(' ')]
            if SOLVE_PART == 1:
                data_array.append(numbers.copy())
            if SOLVE_PART == 2:
                numbers.reverse()
                data_array.append(numbers.copy())
    return data_array


def raise_factors(nums):
    temp_list = []
    for i in range(len(nums) - 1):
        temp_list.append(nums[i + 1] - nums[i])
    return temp_list


def create_prediction_tree(numbers):
    lists = [numbers]
    temp_list = raise_factors(numbers)
    lists.append(temp_list)
    while (prod(temp_list) + sum(temp_list)) != 0:
        temp_list = raise_factors(temp_list)
        lists.append(temp_list)
    return lists


def count_predictions(numbers):
    prediction_list = create_prediction_tree(numbers)
    prediction_list[-1].append(0)
    for i in range(len(prediction_list) - 1, 0, -1):
        prediction_list[i - 1].append(prediction_list[i][-1] + prediction_list[i - 1][-1])
    return prediction_list[0][-1]


def solve():
    data = get_numbers()
    result = []
    for array in data:
        result.append(count_predictions(array))
    return sum(result)


def main():
    print(f'Result of day {DAY} part {SOLVE_PART} is {solve()}.')


if __name__ == '__main__':
    main()

