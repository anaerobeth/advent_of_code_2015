import re

with open('day12_input.txt', 'r') as f:
    for string in f:
        numbers_list = re.findall("(-?\d+)", string)

        print sum(map(int, numbers_list))
