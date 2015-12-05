import re

def enough_vowels(s):
    return sum(letter in 'aeiou' for letter in string) >= 3


def has_doubles(s):
    return re.compile(r"\w*(\w)\1\w*").match(s) != None


def valid(s):
    result = True
    for chars in ['ab', 'cd', 'pq', 'xy']:
        if chars in s:
            result = False
    return result

def message(s, nice):
    if nice == True:
        return "{0} is nice".format(s)
    else:
        return "{0} is naughty".format(s)


with open('day5_input.txt', 'r') as f:
    count = 0
    for line in f:
        string = line.rstrip().lower()
        if enough_vowels(string) and has_doubles(string) and valid(string):
            nice = True
            count += 1
        else:
            nice = False
        print message(string, nice)
    print count
