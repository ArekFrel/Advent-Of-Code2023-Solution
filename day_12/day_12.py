DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 1

my_dict = {}

def shorten(pat:str, cd:list)-> (str, list):
    pat = reduce_double_periods(pat)
    if pat.startswith('.'):
        return shorten(pat[1:], cd)
    if pat.endswith('.'):
        return shorten(pat[0:-1], cd)
    if pat.startswith('#'):
        fcv = cd.pop(0) # stands for first code value
        return shorten(pat[fcv + 1:], cd)
    if pat.endswith('#'):
        lcv = cd.pop() # stands for last code value
        return shorten(pat[:-(lcv + 1)], cd)
    return pat, cd


def reduce_double_periods(text):
    while '..' in text:
        text = text.replace('..', '.')
    return text


def does_align(pat, cd):
    count, arr = 0, []
    for i in range(len(pat)):
        if pat[i] == '#':
            count = count + 1
        if pat[i] == '.':
            if count == 0:
                continue
            arr.append(count)
            count = 0
    if count:
        arr.append(count)
    return cd == arr


def go(pat:str, cd:list, i=0)-> int:
    if len(pat) == 0:
        return 1
    if i == len(pat):
        if does_align(pat, cd):
            return 1
        else:
            return 0
    else:
        if pat[i] == '?':
            return go(pat[0: i] + '#' + pat[i + 1:], cd, i + 1) + go(pat[0: i] + '.' + pat[i + 1:], cd, i + 1)
        if pat[i] in ['.', '#']:
            return go(pat[0: i] + pat[i:], cd, i + 1)

def go_1(pat:str, cd:list, i:int, ci:int, curr:int)-> int:
    # i - position in pattern
    # ci - position in code
    # curr - value in the code
    key = (i, ci, curr)
    if key in my_dict:
        return my_dict[(i, ci, curr)]
    if i == len(pat):
        if ci == len(cd) - 1 and curr == cd[ci]:
            return 1
        if ci == len(cd) and curr == 0:
            return 1
        else:
            return 0
    result  = 0
    if pat[i] == '?':
        for gues in ['.', '#']:
            if gues == '.':
                if curr > 0 and ci < len(cd) and cd[ci] == curr:
                    result += go_1(pat, cd, i + 1, ci + 1, 0)
                elif curr == 0:
                    result += go_1(pat, cd, i + 1, ci, 0)
            elif gues == '#':
                result += go_1(pat, cd, i + 1, ci, curr + 1)

    if pat [i] == '.':
        if curr > 0 and ci < len(cd) and cd[ci] == curr:
            result += go_1(pat, cd, i + 1, ci + 1, 0)
        elif curr == 0:
            result += go_1(pat, cd, i + 1, ci, 0)

    if pat [i] == '#':
        result += go_1(pat, cd, i + 1, ci, curr + 1)

    my_dict[key] = result
    return result


def main() -> None:
    with open(FILE, 'r', encoding='utf-8') as my_input:

        result = 0
        for line in my_input:
            pattern, code = line.strip().split()
            code = [int(_) for _ in code.split(',')]
            if SOLVE_PART == 2:
                pattern = '?'.join([pattern for _ in range(5)])
                # pattern = reduce_double_periods(pattern)
                code = code * 5
            add = go_1(
                pat=pattern,
                cd=code,
                i=0,
                ci=0,
                curr=0)
            print(f'{pattern}    {code}    {add}')
            # with open('result_shorten.txt', 'a', encoding='utf-8') as my_output:
            #     my_output.write(f'{add}\n')
            result +=  add
            my_dict.clear()
        print(result)



if __name__ == '__main__':
    # a = go(shorten('.?#.?.??###', [1,1,4],), 0)
    # print(a)
    # go_1()
    main()




