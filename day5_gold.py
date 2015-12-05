import re

def has_double_doubles(s):
    obj = re.compile(r"(.)(.)(.*(\1)(\2))").findall(s)
    if len(obj) > 0:
        print "Double-doubles: {0}".format(obj)
        return True


def has_skip_repeat(s):
    obj = re.compile(r"(.)((?!\1).)(\1)").findall(s)
    if len(obj) > 0:
        print "Skips: {0}".format(obj)
        return True


with open('day5_input.txt', 'r') as f:
    count = 0
    for line in f:
        string = line.rstrip().lower()
        if has_double_doubles(string) and has_skip_repeat(string):
            nice = True
            count += 1
        else:
            nice = False
    print count
