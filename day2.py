def get_dimensions(line):
    ''' parse each line into a list of smallest to largest dimension '''
    line = sorted(line.rstrip().split('x'), key=int)
    return [int(n) for n in line]


def get_surface_area(l, w, h):
    '''
    surface area of a box: 2*l*w + 2*w*h + 2*h*l
    then add area of the smallest side
    '''
    base_area = 2*l*w + 2*w*h + 2*h*l
    total_area = base_area + l*w
    return total_area

def get_ribbon_length(l, w):
    '''
    shortest distance around its sides or
    the smallest perimeter of any one face
    '''
    return 2*l + 2*w

def get_bow_length(l, w, h):
    ''' cubic feet of volume of the present '''
    return l * w * h


total_square_feet = 0
total_feet_of_ribbon = 0

with open('day2_input.txt', 'r') as f:
    for line in f:
        l, w, h = get_dimensions(line)
        area = get_surface_area(l, w, h)
        total_square_feet = total_square_feet + area

        ribbon = get_ribbon_length(l, w)
        bow = get_bow_length(l, w, h)
        total_feet_of_ribbon = total_feet_of_ribbon + ribbon + bow
        print "Dimension is {0} x {1} x {2}".format(l, w, h)
        print "Ribbon length is {0}".format(ribbon)
        print "Bow length is {0}".format(bow)

print "Square feet of wrapping paper: {0}".format(total_square_feet)
print "Feet of Ribbon: {0}".format(total_feet_of_ribbon)

