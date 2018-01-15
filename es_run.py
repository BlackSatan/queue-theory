import eventstreams
import matplotlib.pyplot as plt
import stats
import numpy as np
import math

sample = eventstreams.test_simple(50, .6)
# sample = eventstreams.exponential_simple(50)
plt.hist(sample)
plt.title('Проміжки часу між подіями')
plt.show()

is_normal = stats.chisquare(sample)
print('Chi^2 acceptance is', is_normal)

if is_normal:
    intensity = eventstreams.normal_sample_intensity(sample)
    print('Stream intensity =', format(intensity, '.9f'))
    exit()

count = eventstreams.intervals_count(sample)

relative_bins = [min(eventstreams.interval_elements(sample, i)) for i in range(0, count)]
relative_bins.append(max(sample))

relative_interval_length = eventstreams.relative_intervals_length(sample)

for i in range(len(relative_bins) - 1):
    plt.plot([relative_bins[i], relative_bins[i + 1]], [relative_interval_length[i], relative_interval_length[i]])

plt.title('Відносні частоти')
plt.show()


lambdas = eventstreams.intervals_intensity(sample)
lambdas_x=np.array(lambdas)
np.set_printoptions(precision=10, suppress=True)
print('Lamdas = ', lambdas_x)

joined_lambdas = eventstreams.join_intervals(sample)
print('Lambdas after aggregation', joined_lambdas)
