def chars_of_string(l):
    return len(l)


def chars_in_memory(l):
    l = l.decode('string_escape')
    return len(l) - 2


with open('day8_input.txt', 'r') as f:
    total_chars_of_string = 0
    total_chars_in_memory = 0

    for line in f:
        l = line.rstrip()
        total_chars_of_string += chars_of_string(l)
        total_chars_in_memory += chars_in_memory(l)

    print total_chars_of_string - total_chars_in_memory

