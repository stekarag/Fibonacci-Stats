import statistics as stat
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import approximate_taylor_polynomial as atp
import scipy
import fiboFunctions.py


print("This program prints stats and graph for Fibonacci sequence.")
n = 0
while not n:
    try:
        n = int(input("Up to which number, less than 91, would you like to calculate? "))
    except ValueError:
        n = 0
    if not n:
        n = 9
        print("Invalid response, n set to default value(n=13)")
    elif n > 91:
        n = 91
        print("Exceeded maximum capacity, n set to 91")

a = createFibonacci(n)
print(f"Length of a is {len(a)}")
cmean = []
cmedian = []
charmonicMean = []
clinearRegression = []
linearAnswer = []
#populate the arrays of the functions, implement solution with map
for i in range(len(a)):
    j = i + 1
    print("Calculating stats for F(%i)=%i" % (j, a[i]))
    mean,median,harmonic = stats(a, j)
    cmean.append(mean)
    cmedian.append(median)
    charmonicMean.append(harmonic)

print("Stats calculated, calculating linear regression...")
i = [x for x in range(len(a))]
linearAnswer = scipy.stats.linregress(i, a)
print(len(linearAnswer))
alr, blr = linearAnswer[0:2]
clinearRegression = [alr*j + blr for j in i]

cpolynomialRegression = np.poly1d(np.polyfit(i, a, 3))
yp = np.linspace(1, n, n + 2)

plotFibonacci(cmean,cmedian,charmonicMean, a, clinearRegression, cpolynomialRegression, yp)
print("Exiting...")
