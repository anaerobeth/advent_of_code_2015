from itertools import combinations

with open('day17_input.txt', 'r') as f:
    containers = []
    valid_combos = 0
    minimum_combos = 0
    eggnog_volume = 150

    for string in f:
        containers.append(string.rstrip())

    for i in range(len(containers) + 1):
        combos = map(list, combinations(containers, i))

        for c in combos:
            if sum(map(int, c)) == eggnog_volume:
                valid_combos += 1

        print 'Number of Containers: {}'.format(i+1)
        print 'Combinations of containers can exactly fit all 150 liters of eggnog'
        print valid_combos




