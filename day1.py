with open('day1_input.txt', 'r') as f:
    ''' final floor is given by the difference between the up and down steps '''
    steps = f.readlines()[0]
    up = steps.count('(')
    down = steps.count(')')

print(up - down)

