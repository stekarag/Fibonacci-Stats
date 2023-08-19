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

