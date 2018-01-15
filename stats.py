import math
import numpy as np
import eventstreams


def normal(p):
    t = math.sqrt(math.log(1 / (p * p)))
    c0 = 2.515517
    c1 = 0.802853
    c2 = 0.010328
    d1 = 1.432788
    d2 = 0.1892659
    d3 = 0.001308
    return t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t)


def prison_kv(p, n):
    return n * math.pow(1 - 2 / (9 * n) + normal(p) * math.sqrt(2 / (9 * n)), 3)


def f_exp_dist(lmbd, x):
    return 1 - math.exp(-lmbd * x)


def chisquare(sample):
    sample_elements_count = len(sample)
    intervals_count = eventstreams.intervals_count(sample)
    h = eventstreams.interval_step(sample)
    avg_r = 1 / np.mean(sample)
    chisquare_result = 0
    for i, interval_length in enumerate(eventstreams.intervals_length(sample)):
        pi = f_exp_dist(avg_r, min(sample) + h * (i + 1)) - f_exp_dist(avg_r, min(sample) + h * i)
        ei = pi * sample_elements_count
        chisquare_result += math.pow(interval_length - ei, 2) / ei
    return chisquare_result <= prison_kv(.05, intervals_count - 1)


def normalize(sample):
    intervals_length = eventstreams.intervals_length(sample)
    intervals_count = eventstreams.intervals_count(sample)
    interval_step = eventstreams.interval_step(sample)
    result = []
    for index in range(0, intervals_count):
        n = intervals_length[index]
        n_i = sum(intervals_length[:index+1])
        if n_i > len(sample):
            n_i = len(sample) - 1
        result.append(n / (len(sample) - n_i * interval_step))
    return result

