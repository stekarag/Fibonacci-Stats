import statistics as stat
import matplotlib.pyplot as plt

def createf(x=100):
    a = [1,1]
    for i in range(x):
        next = a[-1]+a[-2]
        a.append(next)
    
    return a 

def stats(s=[1],x=2):
    mn = stat.mean(s[0:x])
    mdn = stat.median(s[0:x])
    hmn = stat.harmonic_mean(s[0:x])
    #print("Mean is %d\nMedian is %i\nHarmonic mean is %d"%(mn,mdn,hmn))
    return mn,mdn,hmn

def plotF(y1,y2,y3,y):
    print("Running plotF")
    
    y4 = []
    l = len(y1)
    x = range(len(y1))
    
    for i in x:
         y4.append(pow(i,2))

    plt.plot(x,y1,label="Means")
    plt.plot(x,y2,label="Medians")
    plt.plot(x,y3,label="Harmonic Mean")
    plt.plot(x,y,label="Fibonacci")
    plt.plot(x,y4,label="y=x^2",ls="--")
    plt.plot(x,x,label="y=x",ls="--")
    plt.xlabel("x")
    plt.ylabel("y")
    title = "Mean, median, hmean of fibonacci for n=%d"%l
    plt.title(title)
    plt.axhline(y=0, color='#000000')
    plt.axvline(x=0, color='#000000')
    plt.legend()
    plt.show()

print("This program prints stats and graph for Fibonacci sequence.")
n = 0
while not n:
    try:
        n = int(input("Up to which number would you like to calculate? "))
    except ValueError:
        n = 0
    if not n:
        n = 9
        print("Invalid response, n set to default value(n=10)")
    elif n > 123:
        n = 123
        print("Exceeded maximum capacity, n set to 123") 

a = createf(n)
cmn = []
cmdn = []
chmn = []
for i in range(len(a)):
    j = i+1
    print("Calculating stats for F(%i)=%i"%(j,a[i]))
    mn,mdn,hmn = stats(a,j)
    cmn.append(mn)
    cmdn.append(mdn)
    chmn.append(hmn)

plotF(cmn,cmdn,chmn,a)
print("Exiting...")
