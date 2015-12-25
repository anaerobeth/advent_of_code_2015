from itertools import permutations


def parse_instruction(line):
    l = line.rstrip().replace(' to ', ',').replace(' = ', ',')
    return l.split(',')


def get_locations(path, locations):
    if path[0] not in locations:
        locations.append(path[0])
    if path[1] not in locations:
        locations.append(path[1])


def generate_routes(locations):
    for p in permutations(locations):
        routes.append(p)


def calculate_trip_distance(route, distances, trip_distances):
    trip_distance = 0
    end = 'End'
    temp_route = route + (end,)
    print 'Route is: '
    print route
    for index, point in enumerate(route):
        key = point + '-' + temp_route[index + 1]
        trip_distance += int(distances[key])

    print 'Trip distance is: '
    print trip_distance
    trip_distances.append(trip_distance)

def record_distance(path, distances):
    left, right, dist = path
    key = left + '-' + right
    alt_key = right + '-' + left

    for item in [key, alt_key]:
        distances[item] = dist


def add_terminal_locations(locations, distances):
    for location in locations:
        key = location + '-End'
        distances[key] = '0'


with open('day9_input.txt', 'r') as f:
    paths = []
    distances = {}
    locations = []
    routes = []
    trip_distances = []

    for line in f:
        path  = parse_instruction(line)
        paths.append(path)
        get_locations(path, locations)
        record_distance(path, distances)

    generate_routes(locations)
    add_terminal_locations(locations, distances)

    for route in routes:
        calculate_trip_distance(route, distances, trip_distances)

    print 'Shortest distance is: '
    print min(trip_distances)
    print 'Longest distance is: '
    print max(trip_distances)
