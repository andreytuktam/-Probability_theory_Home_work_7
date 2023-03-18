import numpy as np
import scipy.stats as stats

x1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
y1 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
z1 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

# гипотеза Н0 - различий нет
# гипотеза Н1 - есть различия 

print(stats.kruskal(x1, y1, z1))

# принимаем гипотезу Н0 т.к. pvalue > a 