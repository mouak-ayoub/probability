from scipy.stats import bernoulli
import numpy as np
import pandas as pd

'''
This script simulate adam's law of expectation
and eve's law
'''

p1, p2 = 0.5, 0.7
size_sample = 100
number_samples = 10_0
sample_1 = bernoulli(p1)
sample_2 = bernoulli(p2)

expectation, expectation_1, expectation_2=[],[], []

for i in range(number_samples):

    samples = bernoulli(0.5).rvs(size_sample)

    final_samples = [(1, sample_1.rvs()) if sample == 1 else (2, sample_2.rvs()) for sample in samples]

    df = pd.DataFrame.from_records(final_samples, columns=['type', 'value'])

    all_values = df['value']
    expectation.append(all_values.sum())
    values_1 = df[df.type == 1].value
    values_2 = df[df.type == 2].value

    expectation_1.append( values_1.sum())
    expectation_2.append( values_2.sum())

print('**************************************** Expectation ***************************************************************')

print(f' expectation of all sample  is {np.mean(expectation)}')
print(f' expectation of conditional on the first sample type is { np.mean(expectation_1)}')
print(f' expectation of conditional on the second sample type is {np.mean(expectation_2)}')
print(f' verify adam law  is {np.sum([np.mean(expectation_1), np.mean(expectation_2)])}')


print('**************************************** Variance ******************************************************************')
print(f' variance of all sample  is {np.var(expectation)}')
print(f' variance of conditional on the first sample type is {np.var(expectation_1 * 2)}')
print(f' variance of conditional on the second sample type is {np.var(expectation_2 * 2)}')

print(f' mean pf the  conditional variance   on the second sample type is {np.mean([np.var(expectation_1 ), np.var(expectation_2)])}')
print(f' variance of the conditional mean    is {np.var([np.mean(expectation_1) * 2, np.mean(expectation_2 ) / 0.7 ])}')

