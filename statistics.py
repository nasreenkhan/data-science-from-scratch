from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title('Histogram of friend counts')
plt.xlabel('# of friends')
plt.ylabel('# of people')
plt.show()

num_points = len(num_friends) # 204
largest_value = max(num_friends) # 100
smallest_values = min(num_friends) # 1
sorted_values = sorted(num_friends)
smallest_values = sorted_values[0] # 1
second_smallest_value = sorted_values[1] # 1
second_largest_value = sorted_values[-2] # 49

from typing import List

def mean(xs: List[float]) -> float:
    return sum(xs)/len(xs)

mean(num_friends) # 7.333333333333333


def _median_odd(xs: List[float]) -> float:
    """ If len(xs) is odd, the median is the average of middle of two element """
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """ If len(x) is even, it´s the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g length 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(v: List[float]) -> float:
    """ Finds the 'middle-most' value of v """
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2


def quantile(xs: List[float], p:float) -> float:
    """ Returns pth-percentile value in x """
    p_index = int(p*len(xs))
    return sorted(xs)[p_index]


assert quantile(num_friends, 0.1) == 1
assert quantile(num_friends, 0.25) == 3
assert quantile(num_friends, 0.75) == 9
assert quantile(num_friends, 0.90) == 13


def mode(x: List[float]) -> List[float]:
    """ Returns a list, since there might be more than one mode """
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


assert set(mode(num_friends)) == {1,6}


def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


assert data_range(num_friends) == 99


from linear_algebra import sum_of_squares


def de_mean(xs: List[float]) -> List[float]:
    """ Translate xs by substracting its mean (so the result has mean 0) """
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
    """ Almost the avarage squares deviation from the mean """
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deveations = de_mean(xs)
    return sum_of_squares(deveations) / (n - 1)

assert 81.54 < variance(num_friends) < 81.55


import math


def standard_deviation(xs: List[float]) -> float:
    """ Standard deviation is the square root of the variance """
    return math.sqrt(variance(xs))

assert 9.02 < standard_deviation(num_friends) < 9.04


def interquantile_range(xs: List[float]) -> float:
    """ Returns the diference between the 75%-ile and the 25%-ile """
    return quantile(xs, 0.75) - quantile(xs, 0.25)

assert interquantile_range(num_friends) == 6