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


def locate_house(x, y, move_x, move_y):
    x += move_x
    y += move_y
    cell = "{0},{1}".format(x, y)
    return x, y, cell

def houses_with_presents(santas = 1):
    with open('day3_input.txt', 'r') as f:
        steps = f.readlines()[0].rstrip()
        santa_x, santa_y, robo_x, robo_y = 0, 0, 0, 0
        house_locations = ['0,0']
        for index, value in enumerate(steps):
            move_x, move_y = translate_symbol_to_move(value)
            if santas == 2:
                if index % 2 == 0:
                    santa_x, santa_y, location = locate_house(santa_x, santa_y, move_x, move_y)
                else:
                    robo_x, robo_y, location = locate_house(robo_x, robo_y, move_x, move_y)
            elif santas == 1:
                santa_x, santa_y, location = locate_house(santa_x, santa_y, move_x, move_y)
            else:
                raise Exception('Maximum of two santas, please')
            house_locations.append(location)
    return len(set(house_locations))

print houses_with_presents()
print houses_with_presents(santas = 2)
print houses_with_presents(santas = 3)
