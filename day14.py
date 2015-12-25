import re

def get_stats(reindeer, string):
    speed, flight_time, rest_time = re.findall("(\d+)", string)
    stats[reindeer] = {}
    stats[reindeer]['flight'] = flight_time
    stats[reindeer]['rest'] = rest_time
    stats[reindeer]['speed'] = speed

    return stats

with open('day14_input.txt', 'r') as f:
    stats = {}
    for string in f:
        reindeer = string.split(' ')[0]
        get_stats(reindeer, string)


    print stats
    print stats[reindeer]



