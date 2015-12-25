import re
import bisect


def validate_object(new_string, level=0):
    adjustment = 0
    o_count = new_string.count('{')
    c_count = new_string.count('}')
    adjustment = c_count - o_count
    print adjustment
    if adjustment == 0:
        print 'valid string'
    elif adjustment > 0:
        if level > 0:
            print 'STILL MISSING'
        else:
            print 'MISSING OPEN'
    else:
        if level > 0:
            print 'STILL MISSING'
        else:
            print 'MISSING CLOSE'
    print new_string
    return adjustment

with open('day12_input.txt', 'r') as f:
    red_indexes = []
    open_brace_indexes = []
    close_brace_indexes = []
    fails = 0
    for string in f:
        numbers_list = re.findall("(-?\d+)", string)
        total = sum(map(int, numbers_list))

        o = re.compile('{')
        open_braces = o.finditer(string)
        for item in open_braces:
            open_brace_indexes.append(item.start(0))

        c = re.compile('}')
        close_braces = c.finditer(string)
        for item in close_braces:
            close_brace_indexes.append(item.start(0))

        p = re.compile(':"red"')
        red_indexes = p.finditer(string)
        for item in red_indexes:
            # print 'index of red:'
            num = item.start(0)
            # print num
            obi = bisect.bisect(open_brace_indexes, num)
            # print 'closest open brace is on:'
            start_of_object = open_brace_indexes[obi-1]
            # print start_of_object
            cbi = bisect.bisect(close_brace_indexes, num)
            # print 'closest close brace is on:'
            end_of_object = close_brace_indexes[cbi]
            # print end_of_object
            new_string = string[start_of_object:end_of_object+1]
            adjustment = validate_object(new_string)

            if adjustment > 0:
                start_index = open_brace_indexes.index(start_of_object)
                adjusted_start_of_object = open_brace_indexes[start_index - adjustment]
                adjusted_string = string[adjusted_start_of_object:end_of_object+1]
                print adjusted_string

                adjustment = validate_object(adjusted_string, 1)

                start_index += adjustment
                if adjustment == 0:
                    print 'ADJUSTMENT COMPLETE'
                else:
                    adjusted_start_of_object = open_brace_indexes[start_index - adjustment]
                    adjusted_string = string[adjusted_start_of_object:end_of_object+1]
                    print adjusted_string
                    adjustment = validate_object(adjusted_string, 2)
                    start_index += adjustment
                    if adjustment != 0:
                        print 'FAILED ON THIRD'
                        adjusted_start_of_object = open_brace_indexes[start_index - adjustment]
                        adjusted_string = string[adjusted_start_of_object:end_of_object+1]
                        print adjusted_string
                        adjustment = validate_object(adjusted_string, 2)
                        if adjustment != 0:
                            fails += 1
                            print 'FAILED ON FOURTH'

            elif adjustment < 0:
                close_index = close_brace_indexes.index(end_of_object)
                adjusted_end_of_object = close_brace_indexes[close_index + adjustment]
                adjusted_string = string[start_of_object:adjusted_end_of_object+1]
                print adjusted_string

                adjustment = validate_object(adjusted_string, 1)

                close_index += adjustment
                if adjustment == 0:
                    print 'ADJUSTMENT COMPLETE'
                else:
                    adjusted_close_of_object = close_brace_indexes[close_index - adjustment]
                    adjusted_string = string[adjusted_start_of_object:end_of_object+1]
                    adjustment = validate_object(adjusted_string, 2)
                    close_index += adjustment
                    if adjustment != 0:
                        print 'FAILED ON THIRD'
                        try:
                            adjusted_close_of_object = close_brace_indexes[close_index - adjustment]
                        except IndexError as err:
                            print err

                        adjusted_string = string[adjusted_start_of_object:end_of_object+1]
                        adjustment = validate_object(adjusted_string, 2)
                        if adjustment != 0:
                            fails += 1
                            print 'FAILED ON FOURTH'
        print fails
        # print close_brace_indexes
