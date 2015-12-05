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
    x = 0
    y = 0
    for value in steps:
        move_x, move_y = translate_symbol_to_move(value)
        x = x + move_x
        y = y + move_y
        cell = "{0},{1}".format(x,y)
        house_locations.append(cell)

print house_locations
print len(set(house_locations))

