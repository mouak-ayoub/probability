from scipy import stats

import numpy as np
import matplotlib.pylab as plt

number_samples = 1_000

money_received = []

envelope_one = stats.uniform().rvs(number_samples)
envelope_two = stats.uniform().rvs(number_samples)

samples = [stats.bernoulli(envelope_one[i]).rvs() for i in range(number_samples)]

money_received = np.where(np.array(samples) == 1, envelope_one, envelope_two)

max_envelope = np.maximum(envelope_one, envelope_two)
max_match = (max_envelope == money_received)
print(np.mean(money_received))
print(f'the probability of getting the maximum is {max_match.sum() / number_samples}')
