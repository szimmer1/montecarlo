#!/usr/bin/env python

from random import random
from math import ceil

def roll(num_dice, num_rolls):
    """
    Returns a generator of tuples, where len(generator) == num_rolls and len(tuple) == num_dice
    """
    for _ in xrange(num_rolls):
        yield tuple(ceil(6 * random()) for _ in xrange(num_dice))

def eval_prob(rolls, fn):
    """
    Takes a 'roll' generator and fn to evaluate the roll (return binary t/f)
    Returns the %(true / false) evaluations, or essentially the empirical probability
    B/c a generator is used, all the data is never in memory at one time (scalable)
    """
    t = f = 0
    for roll in rolls:
        if fn(roll):
            t = t + 1
        else:
            f = f + 1
    total = t + f
    #print "t={}, f={}, total={}".format(t, f, total)
    return t / float(total) * 100.0 if total != 0 else None

events = {
    'at_least_one_six': lambda tup: reduce(lambda x,y: x or y, map(lambda n: n == 6, tup))
}

if __name__ == "__main__":
    num_rolls = 100000
    num_dice = 3
    print eval_prob(roll(num_dice, num_rolls), events['at_least_one_six'])
