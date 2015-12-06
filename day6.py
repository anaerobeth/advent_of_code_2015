import pandas as pd
import numpy as np

def build_grid(coord):
    a, b, c, d = map(int, coord.split(','))
    grid = []
    for x in range(a, c + 1):
        for y in range(b, d + 1):
            grid.append([x, y])
    print 'Grid size is ', len(grid)
    return grid


def turn_on(grid):
    for loc in grid:
        df[loc[0]][loc[1]] = 1


def turn_off(grid):
    for loc in grid:
        df[loc[0]][loc[1]] = np.nan


def toggle(grid):
    for loc in grid:
        df[loc[0]][loc[1]] = np.nan if df[loc[0]][loc[1]] == 1 else 1


def parse_instruction(string):
    substrings = string.split(' ')
    command = substrings[-4]
    l = "{0},{1}".format(substrings[-3], substrings[-1])
    return command, l


with open("day6_input.txt", "r") as f:
    df = pd.DataFrame(index=np.arange(1000), columns=np.arange(1000))
    print 'Df nulls at the start: ', df.isnull().sum().sum()

    for line in f:
        string = line.rstrip().lower()
        command, coord = parse_instruction(string)
        grid = build_grid(coord)
        if command == 'off':
            turn_off(grid)
        elif command == 'on':
            turn_on(grid)
        elif command == 'toggle':
            toggle(grid)
        else:
            print 'Invalid instructions'
    print 'Df nulls at the end: ', df.isnull().sum().sum()
    n = df.isnull().sum().sum()
    on = (1000 * 1000) - n
    print "Total ON lights is {0}".format(on)
