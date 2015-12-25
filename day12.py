import re
import bisect

with open('day12_input.txt', 'r') as f:
    red_indexes = []
    open_brace_indexes = []
    close_brace_indexes = []
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
            o_count = new_string.count('{')
            c_count = new_string.count('}')
            if o_count == c_count:
                print 'valid string'
            elif o_count < c_count:
                print 'MISSING OPEN'
                print new_string
                adjustment = c_count - o_count
                print adjustment
                start_index = open_brace_indexes.index(start_of_object)
                adjusted_start_of_object = open_brace_indexes[start_index - adjustment]
                adjusted_string = string[adjusted_start_of_object:end_of_object+1]
                print adjusted_string
                ao_count = adjusted_string.count('{')
                ac_count = adjusted_string.count('}')
                if ao_count == ac_count:
                    print 'valid adjusted string'
                else:
                    print 'STILL FAILING'

            else:
                print 'MISSING CLOSE'
                print new_string
                adjustment = o_count - c_count
                print adjustment
                close_index = close_brace_indexes.index(end_of_object)
                adjusted_end_of_object = close_brace_indexes[close_index + adjustment]
                adjusted_string = string[start_of_object:adjusted_end_of_object+1]
                print adjusted_string

                ao_count = adjusted_string.count('{')
                ac_count = adjusted_string.count('}')
                if ao_count == ac_count:
                    print 'valid adjusted string'
                else:
                    print 'STILL FAILING'

        # print close_brace_indexes
