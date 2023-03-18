import numpy as np
import scipy.stats as stats

x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])

# гипотеза Н0 - различий нет
# гипотеза Н1 - есть различия 

print(stats.mannwhitneyu(x1, y1))

# принимаем гипотезу Н0 т.к. pvalue > a 
