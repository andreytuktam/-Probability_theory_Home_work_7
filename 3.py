import numpy as np
import scipy.stats as stats

x1 = np.array([150, 160, 165, 145, 155])
y1 = np.array([140, 155, 150, 130, 135])

# гипотеза Н0 - различий нет
# гипотеза Н1 - есть различия 

print(stats.wilcoxon(x1, y1))

# принимаем гипотезу Н0 т.к. pvalue > a 