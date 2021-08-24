from collections import namedtuple
import math


Case = namedtuple('Case', 'case repeat payoff')


outcomes = {
    '840': Case(840, 6, +300),
    '831': Case(831, 6, +100),
    '822': Case(822, 3, +120),
    '750': Case(750, 6, +60),
    '741': Case(741, 6, +40),
    '732': Case(732, 6, +15),
    '660': Case(660, 3, +100),
    '651': Case(651, 6, +10),
    '642': Case(642, 6, +5),
    '633': Case(633, 3, +5),
    '552': Case(552, 3, +5),
    '543': Case(543, 6, -30),
    '444': Case(444, 1, +5),
}


nCr = math.comb
nPr = lambda n, r: nCr(n, r) * math.factorial(r)


def cal_prob(case):
    a, b, c = list(map(int, str(case.case)))
    # combinations of a, b, c marbles from 3 different colors, then permutates the colors if distinct
    # total number of possible outcomes would be combination of 12 out of 24 marbles
    prob = nCr(8, a) * nCr(8, b) * nCr(8, c) * case.repeat / nCr(24, 12)
    # expected reward
    expR = prob * case.payoff
    # result
    Result = namedtuple('Result', 'case prob payoff expR')
    return Result(case.case, prob, case.payoff, expR)
