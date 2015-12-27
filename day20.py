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


def calculate_presents_with_cap(house, elf_tracker):
    all_factors = get_factors(house)
    print all_factors
    for elf, visits in elf_tracker.items():
        if elf in all_factors:
            elf_tracker[elf] += 1

    for factor in all_factors:
        if elf_tracker[factor] > 50:
            print "Elf {} has visited {} times".format(factor, elf_tracker[factor])
            all_factors.remove(factor)
    print "new factor set: {}".format(all_factors)
    presents = reduce(lambda x, y: x + y, all_factors) * 11

    return presents, elf_tracker


target = 2000

elf_tracker = {}
# i narrowed down the range by calculating presents for selected house numbers until the target is exceeded
# for house in range(6, 700):
#     presents = calculate_presents(house)

#     if presents >= target:
#         print 'Lowest number of house with at least the target number of presents: {}'.format(house)
#         break


for house in range(1, 150):
    elf_number = house
    elf_tracker[elf_number] = 0

    presents, elf_tracker = calculate_presents_with_cap(house, elf_tracker)

    if presents >= target:
        print 'Lowest number of house with at least the target number of presents: {}'.format(house)
        break
