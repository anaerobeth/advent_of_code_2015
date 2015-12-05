def translate_symbol_to_move(value):
    '''
    Moves are always exactly one house to the
    north (^), south (v), east (>), or west (<)
    '''
    moves = {
        '^': [0, 1],
        'v': [0, -1],
        '>': [1, 0],
        '<': [-1, 0]
        }
    return moves.get(value)


house_locations = ['0,0']

with open('day3_input.txt', 'r') as f:
    steps = f.readlines()[0].rstrip()
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0
    for index, value in enumerate(steps):
        move_x, move_y = translate_symbol_to_move(value)
        if index % 2 == 0:
            santa_x = santa_x + move_x
            santa_y = santa_y + move_y
            cell = "{0},{1}".format(santa_x,santa_y)
        else:
            robo_x = robo_x + move_x
            robo_y = robo_y + move_y
            cell = "{0},{1}".format(robo_x,robo_y)
        house_locations.append(cell)

print house_locations
print len(set(house_locations))

