from scipy import stats

import numpy as np
import matplotlib.pylab as plt

number_samples = 1000
b = 5
a = 3
normal = stats.norm(0, 1)
x_samples = normal.rvs(number_samples)
y_samples = a + b * x_samples + normal.rvs(number_samples)
plt.scatter(x_samples, y_samples)
plt.show()
covariance_matrix = np.cov(x_samples, y_samples)
b_approx = covariance_matrix[0][1] / covariance_matrix[0][0]
a_approx = np.mean(y_samples) - b_approx * np.mean(x_samples)
print(f' b is :{b_approx}')
print(f' a is :{a_approx}')
