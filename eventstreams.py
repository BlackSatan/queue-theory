import math
import random
import numpy as np
import math

def test_simple(_n, _prob):
    result = []
    time = 0
    while _n > 0:
        time += 1
        if random.random() >= _prob:
            _n -= 1
            result.append(time)
    return result


def exponential_simple(_n):
    sample = np.random.exponential(size=_n)
    sample.sort()
    return list(map(lambda x: math.floor(x * 10000), sample))


def intervals_count(_simple):
    _count = len(_simple)
    return math.floor(_count ** (1/3)) if _count > 100 else math.floor(math.sqrt(_count))


def interval_step(_simple):
    _max = max(_simple)
    _min = min(_simple)
    return (_max - _min) / intervals_count(_simple)


def interval_elements(_simple, i):
    _intervals_count = intervals_count(_simple)
    _interval_step = interval_step(_simple)
    _interval_start = 0 if i == 0 else _interval_step * i
    _interval_end = max(_simple) if i == _intervals_count - 1 else _interval_step * (i + 1)
    return [item for item in _simple if _interval_end >= item > _interval_start]


def intervals_length(_simple):
    _intervals_count = intervals_count(_simple)
    return [len(interval_elements(_simple, i)) for i in range(0, _intervals_count)]


def relative_intervals_length(_simple):
    return [i / len(_simple) for index, i in enumerate(intervals_length(_simple))]


def interval_intensity(_simple, i):
    _step = interval_step(_simple)
    _interval_elements = interval_elements(_simple, i)
    return len(_interval_elements) / ((sum(_simple) - sum(_interval_elements)) * _step)


def intervals_intensity(_simple):
    _intervals_count = intervals_count(_simple)
    return [interval_intensity(_simple, i) for i in range(0, _intervals_count)]


def normal_sample_intensity(_sample):
    return 1 / np.mean(_sample) / len(_sample)


def join_intervals(_sample):
    _intensity = intervals_intensity(_sample)
    result_intervals = []
    for i in range(0, len(_intensity) - 1, 2):
        if len(_intensity) - 1 < i + 1:
            result_intervals.append(_intensity[i])
        else:
            intervals_v = interval_v(_sample, _intensity[i], _intensity[i + 1], i, i + 1)
            if intervals_v < 0.2707:
                result_intervals.append(join_intervals_intensity(_sample, i, i + 1))
            else:
                result_intervals.append(_intensity[i])
                result_intervals.append(_intensity[i + 1])
    return result_intervals


def join_intervals_intensity(_sample, first_index, second_index):
    _first_interval = interval_elements(_sample, first_index)
    _second_interval = interval_elements(_sample, second_index)
    return (len(_first_interval) + len(_second_interval)) / (
        (sum(_sample) - sum(_first_interval)) * (
            interval_delta_t(_sample, first_index) + interval_delta_t(_sample, second_index)
        )
    )


def interval_delta_t(_sample, index):
    _intervals_count = intervals_count(_sample)
    previous_t = 0
    if index > 0:
        _previous_interval = interval_elements(_sample, index - 1)
        previous_t = max(_previous_interval) / _intervals_count
    _current_interval = interval_elements(_sample, index)
    current_t = max(_current_interval) / _intervals_count
    return current_t - previous_t


def interval_v(_sample, lambda_first, lambda_second, first_index, second_index):
    _first_interval_len = len(interval_elements(_sample, first_index))
    _second_interval_len = len(interval_elements(_sample, second_index))
    return (lambda_second - lambda_first) / math.sqrt(
        (
            (_first_interval_len - 1) * lambda_second**2 + (_second_interval_len - 1) * lambda_first**2
        ) * math.sqrt(
            _first_interval_len * _second_interval_len * (
                _first_interval_len + _second_interval_len - 2
            ) / (
                _first_interval_len + _second_interval_len
            )
        )
    )
