import re

def run_race(race_duration, flight_time, rest_time, speed):
    leg_time = flight_time + rest_time
    completed_legs = race_duration / leg_time
    last_leg = race_duration % leg_time
    assert completed_legs * leg_time + last_leg == race_duration

    completed_legs_distance = completed_legs * flight_time * speed

    if last_leg >= flight_time:
        last_leg_distance = flight_time * speed
    else:
        last_leg_distance = last_leg * speed

    return completed_legs_distance + last_leg_distance


def get_stats(reindeer, string, race_duration):
    speed, flight_time, rest_time = map(int, re.findall("(\d+)", string))
    stats[reindeer] = {}
    stats[reindeer]['flight'] = flight_time
    stats[reindeer]['rest'] = rest_time
    stats[reindeer]['speed'] = speed

    race_result = run_race(race_duration, flight_time, rest_time, speed)
    results[reindeer] = race_result

    return results

with open('day14_input.txt', 'r') as f:
    stats = {}
    results = {}
    race_duration = 2503
    for string in f:
        reindeer = string.split(' ')[0]
        get_stats(reindeer, string, race_duration)

    sorted_results = sorted(results.items(), key=lambda x: x[1])
    print 'Distance traveled by the winning reindeer: '
    print sorted_results
