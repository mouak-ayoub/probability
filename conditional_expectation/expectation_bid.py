from scipy import stats

import numpy as np
import matplotlib.pylab as plt

bids = stats.uniform().rvs(10)
expectation_dict = {}
for b in bids:
    print(f'the bid is {b}')
    V = stats.uniform()
    samples = V.rvs(1000000)
    samples_filtered = samples[samples < (1.5 * b)]
    print(np.mean(samples_filtered))
    print(3 * b / 4)
    expectation = (np.mean(samples_filtered) - b) * 1.5 * b
    expectation_dict[b] = expectation

print(expectation_dict)
lists = sorted(expectation_dict.items())
x, y = zip(*lists)
print(x, y)
plt.plot(x, y)
plt.show()
