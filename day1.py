with open('day1_input.txt', 'r') as f:
    ''' final floor is given by the difference between the up and down steps '''
    steps = f.readlines()[0]
    up = steps.count('(')
    down = steps.count(')')

print(up - down)

with open('day1_input.txt', 'r') as f:
    ''' Santa enters the basement when the current_floor is -1'''
    current_floor = 0
    steps = f.readlines()[0]
    for index, value in enumerate(steps):
        if value == '(':
            current_floor += 1
        else:
            current_floor -= 1

        if current_floor == -1:
            print index + 1
            break

