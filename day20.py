from itertools import combinations
from functools import reduce


def prime_factors(n):
    i = 2 
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def get_factors(house):
    primes = prime_factors(house)
    factors = [1, house]

    for i in range(1, len(primes) + 1):
        combos = map(list, combinations(primes, i))
        for c in combos:
            factors.append(reduce(lambda x,y: x*y, c))

    return list(set(factors))


def calculate_presents(house):
    all_factors = get_factors(house)
    presents = reduce(lambda x, y: x + y, all_factors) * 10

    return presents


target = 29000000

# i narrowed down the range by calculating presents for selected house numbers until the target is exceeded
for house in range(600000, 700000):
    presents = calculate_presents(house)

    if presents >= target:
        print 'Lowest number of house with at least the target number of presents: {}'.format(house)
        break

