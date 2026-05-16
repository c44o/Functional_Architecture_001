from functools import reduce
from itertools import product

def pairs(xs):
    if not xs:
        return tuple()

    return ((xs[0], xs[1]),) + pairs(xs[2:])

def inside(n, m):
    return lambda cell: 1 <= cell[0] <= n and 1 <= cell[1] <= m

def neighbors(cell):
    x, y = cell

    return (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    )




def valid_neighbors(n, m, cell):
    return set(filter(inside(n, m), neighbors(cell)))


def expand_one_day(n, m, captured):
    return reduce(
        lambda acc, cell: acc | valid_neighbors(n, m, cell),
        captured,
        captured,
    )


def simulate(n, m, target, captured, day):
    if captured == target:
        return day

    return simulate(
        n,
        m,
        target,
        expand_one_day(n, m, captured),
        day + 1,
    )

def ConquestCampaign(N, M, L, battalion):
    target = set(product(range(1, N + 1), range(1, M + 1)))
    captured = set(pairs(battalion))
    return simulate(N, M, target, captured, 1)


print(ConquestCampaign(3, 4, 2, [2, 2, 3, 4]))
# 3
