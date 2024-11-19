import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating distribution
x = [10.1, 12.2, 9.3, 12.4, 13.7, 11.1, 13.3, 10.8, 11.6, 10.1, 11.2, 11.4, 11.8, 7.1,
     12.2, 12.6, 9.2, 14.2, 10.5]
df = pd.DataFrame(x)

stats = df.describe()
print(stats)
h = 1
max_x = round(max(x) + 0.5)
min_x = round(min(x) + 0.5)
n_bins = np.arange(min_x, max_x, h)
fig, axs = plt.subplots(1, 1,
                        figsize=(10, 7),
                        tight_layout=True)

axs.hist(x, bins=n_bins, density=True)
fig.show()

fig2, axs2 = plt.subplots(1, 1,
                          figsize=(10, 7),
                          tight_layout=True)
axs2.boxplot(x)
fig2.show()
plt.show(

)
# Show plot
