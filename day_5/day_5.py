import functools
import time

DAY = '05'
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2
TOTAL_LEN_RANGE = 0

with open(FILE, 'r', encoding='utf-8') as my_input:
    ARRAY = [line for line in my_input]

MAPS = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location'
]


def get_seeds_01():
    for line in ARRAY:
        if "seeds" in line:
            numbers = line.split(':')[1]
            numbers = numbers.strip().rstrip().split(' ')
            numbers_list = [int(num) for num in numbers]
            return numbers_list


def get_seeds_02():
    seeds = []
    for line in ARRAY:
        if "seeds" in line:
            numbers = line.split(':')[1]
            numbers = numbers.strip().rstrip().split(' ')
            numbers_list = [int(num) for num in numbers]
            while numbers_list:
                start_range = numbers_list.pop(0)
                len_of_range = numbers_list.pop(0)
                seeds.append(range(start_range, start_range + len_of_range))
            return seeds


def get_map(text):
    arr = ARRAY
    index = arr.index(f'{text} map:\n')
    i = index + 1
    data = []
    while i <= len(arr) - 1 and arr[i].strip() != '':
        data.append([int(x) for x in arr[i].split(' ')])
        i += 1
    return data


def create_cache():
    result = {}
    for text in MAPS:
        data = get_map(text)
        result[text] = data
    return result


def find_destination(source, the_map):
    for line_map in the_map:
        start_destination, start_source, len_range = line_map
        if source < start_source:
            continue
        if start_source <= source < start_source + len_range:
            return start_destination + (source - start_source)
    return source


def find_destination_02(source, the_map):
    dist_to_edge = None
    for line_map in the_map:
        start_destination, start_source, len_range = line_map
        if start_source <= source < start_source + len_range:
            dist_to_edge = start_source + len_range - source - 1
            return start_destination + (source - start_source), dist_to_edge
    return source, dist_to_edge


def solve(seeds):
    locations = []
    map_dictionary = create_cache()
    for seed in seeds:
        source = seed
        for the_map in MAPS:
            source = find_destination(source, map_dictionary.get(the_map))
            # source = find_destination(source, get_map(the_map))


        locations.append(source)

    seed_to_locations = list(zip(seeds, locations))
    closest_seed_location = min(seed_to_locations, key=lambda x: x[1])
    seed_of_closest_loaction, closeset_location = closest_seed_location

    print(f'Result of day {DAY} part {SOLVE_PART} is {closeset_location}.')


def solve_02(seeds_ranges):
    map_dictionary = create_cache()
    min_location = 1000000000000000000000000000
    for seed_range in seeds_ranges:
        dist_to_edge = 0
        for seed in seed_range:
            if dist_to_edge > 0:
                dist_to_edge -= 1
                continue
            source = seed
            for the_map in MAPS:
                source, dist = find_destination_02(source, map_dictionary.get(the_map))
                if dist and (dist_to_edge > dist or dist_to_edge == 0):
                    dist_to_edge = dist
            if source < min_location:
                min_location = source
                print(f'minimum location has been found {min_location}')

    print(f'Result of day {DAY} part {SOLVE_PART} is {min_location}.')



def main():
    if SOLVE_PART == 1:
        solve(get_seeds_01())
    if SOLVE_PART == 2:
        solve_02(get_seeds_02())


if __name__ == '__main__':
    main()
