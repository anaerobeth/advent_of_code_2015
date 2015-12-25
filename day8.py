def chars_of_string(l):
    return len(l)


def chars_in_memory(l):
    l = l.decode('string_escape')
    return len(l) - 2


def chars_of_encoded_string(l):
    num_of_quote_chars = l.count('"')
    num_of_chars = len(repr(l)) + num_of_quote_chars
    return num_of_chars


with open('day8_input.txt', 'r') as f:
    total_chars_of_strings = 0
    total_chars_in_memory = 0
    total_chars_of_encoded_strings = 0

    for line in f:
        l = line.rstrip()
        total_chars_of_strings += chars_of_string(l)
        total_chars_in_memory += chars_in_memory(l)
        total_chars_of_encoded_strings += chars_of_encoded_string(l)

    print 'Number of characters for string literals minus the number of characters in memory:'
    print total_chars_of_strings - total_chars_in_memory

    print 'Number of characters of encoded string minus the number of characters for string literals:'
    print total_chars_of_encoded_strings - total_chars_of_strings
