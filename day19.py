import re
from random import shuffle

def parse_input(instructions):
    starting_molecule = ''.join(instructions[-1])
    instructions = instructions[:-2]
    elements = re.findall("([A-Z][a-z]?)", starting_molecule)

    return starting_molecule, instructions, elements


def has_converged(temp, previous_temp):
    return True if temp == previous_temp else False



with open('day19_input.txt') as f:
    instructions = []
    molecules = []

    for line in f:
        instructions.append(line.rstrip().split(' => '))

    starting_molecule, instructions, elements = parse_input(instructions)

    for instruction in instructions:
        for index, element in enumerate(elements):
            temp = elements[:]
            if instruction[0] == element:
                temp[index] = instruction[1]
                molecules.append(''.join(temp))

    print 'Number of distinct molecules can be created:'
    print len(set(molecules))

