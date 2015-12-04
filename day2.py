def get_dimensions(line):
    ''' parse each line into a list of smallest to largest dimension '''
    line = sorted(line.rstrip().split('x'), key=int)
    return [int(n) for n in line]


def get_surface_area(line):
    '''
    surface area of a box: 2*l*w + 2*w*h + 2*h*l
    then add area of the smallest side
    '''
    l, w, h = line
    base_area = 2*l*w + 2*w*h + 2*h*l
    total_area = base_area + l*w
    return total_area


total_square_feet = 0
with open('day2_input.txt', 'r') as f:
    for line in f:
        dim = get_dimensions(line)
        area = get_surface_area(dim)
        total_square_feet = total_square_feet + area

print total_square_feet

