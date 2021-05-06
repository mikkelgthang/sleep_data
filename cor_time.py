import numpy as np
import matplotlib.pyplot as plt
import itertools

n1_x = [16.2, 22.9, 20.3, 21.1, 22, 39.1]
n1_y = [12, 13, 21.1, 13.6, 44.5, 56.3]

s1_x = [39.4, 32.7, 12.4, 14.2, 10.4]
s1_y = [71.9, 26, 23.8, 12.1, 30.5]

n2_x = [24.42, 25.33, 20.80, 25.52, 28.49]
n2_y = [13.13, 29.28, 22.86, 20.19, 27.10]

s2_x = [59.26, 46.14, 19.26, 49.35, 39.88]
s2_y = [22.68, 19.85, 22.92, 19.53, 10.24]

n3_x = [34.8, 14.1, 23.7, 16.2, 15.0]
n3_y = [22.3, 24.7, 11.0, 47.1, 44.6]

s3_x = [16.6, 49.0, 32.3, 25.8, 31.6]
s3_y = [26.1, 43.6, 16.4, 13.5, 59.4]

x = list(itertools.chain(n1_x, s1_x, n2_x, s2_x, n3_x, s3_x))
y = list(itertools.chain(n1_y, s1_y, n2_y, s2_y, n3_y, s3_y))

print('Number of datapoints: {}'.format(len(x)))

rho = np.corrcoef(x,y)[1,0]

plt.scatter(x,y)
plt.title('Correlation = {:.2f}'.format(rho))
plt.xlabel('Completion time mission 1: Reading info')
plt.ylabel('Completion time mission 2: Ranking sleep')
plt.show()