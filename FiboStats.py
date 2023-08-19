import statistics as stat
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import approximate_taylor_polynomial as atp
import scipy


def createFibonacci(x=100):
    a = [1,1]
    for i in range(x):
        next = a[-1]+a[-2]
        a.append(next)
    
    return a
 
#Define the statistic measures
def stats(s=[1],x=2):
    mean = stat.mean(s[0:x])
    median = stat.median(s[0:x])
    harmonic = stat.harmonic_mean(s[0:x])
    #print("Mean is %d\nMedian is %i\nHarmonic mean is %d"%(mn,mdn,hmn))
    return mean,median,harmonic


#plot the functions
def plotFibonacci(y1, y2, y3, y, ylr, ypr, yp):
    print("Running plotF")
    
    y4 = []
    l = len(y1)
    x = range(len(y1))
    
    #For the definition y=x^2
    for i in x:
         y4.append(pow(i, 2))

    plt.plot(x, y1, label="Means")
    plt.plot(x, y2, label="Medians")
    plt.plot(x, y3, label="Harmonic Mean")
    plt.plot(x, y, label="Fibonacci")
    plt.plot(x, ylr, label="lin.regression", ls="-.")
    plt.plot(x, ypr(yp), label="Polynomial Regression", ls=":")
    
    '''
    xa = np.linspace(0,l, num=l)
    for degree in np.arange(1,9,step=1): #find intersection point
        taylor = atp(y1,y1[l/2],degree,1)
    plt.plot(x,)
    '''
    plt.xlabel("x")
    plt.ylabel("y")
    title = "Mean, median, hmean of fibonacci for n=%d" % l
    plt.title(title)
    plt.axhline(y=0, color='#000000')
    plt.axvline(x=0, color='#000000')
    plt.legend()
    plt.show()


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
