import numpy as np
import scipy.stats as stats

x1 = np.array([150, 160, 165, 145, 155])
y1 = np.array([140, 155, 150, 130, 135])
z1 = np.array([130, 130, 120, 130, 125])

# гипотеза Н0 - различий нет
# гипотеза Н1 - есть различия 

print(stats.friedmanchisquare(x1, y1, z1))

# принимаем гипотезу Н1 т.к. pvalue < a 