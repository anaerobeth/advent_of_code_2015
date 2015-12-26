import re

def is_flying(timepoint, flight, rest):
    leg_time = flight + rest
    current_leg = timepoint % leg_time
    if current_leg >= flight:
        return False
    else:
        return True


def run_race(race_duration, stats):
    for reindeer in stats:
        distances[reindeer] = 0
        results[reindeer] = 0

    for n in range(0, race_duration ):
        for reindeer, stat in stats.items():
            if is_flying(n, stat['flight'], stat['rest']):
                distances[reindeer] +=  stat['speed']

        winning_distance = sorted(distances.items(), key=lambda x: x[1])[-1][1]
        for reindeer, distance in distances.items():
            if distance == winning_distance:
                results[reindeer] += 1

    return results


def get_stats(reindeer, string, race_duration):
    speed, flight_time, rest_time = map(int, re.findall("(\d+)", string))
    stats[reindeer] = {}
    stats[reindeer]['flight'] = flight_time
    stats[reindeer]['rest'] = rest_time
    stats[reindeer]['speed'] = speed

    return stats


with open('day14_input.txt', 'r') as f:
    stats = {}
    results = {}
    distances = {}
    race_duration = 2503

    assert is_flying(10, 11, 5)

    for string in f:
        reindeer = string.split(' ')[0]
        get_stats(reindeer, string, race_duration)

    results = run_race(race_duration, stats)

    print 'The winning reindeer earned the ff. points:'
    print sorted(results.items(), key=lambda x: x[1])[-1][1]
