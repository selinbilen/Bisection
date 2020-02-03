import math
def bisection(a,b):
    m=(a+b)/2
    while(abs(f(m))>10**-5):
        if(f(a)*f(m)<0):
            b=m

        elif(f(b)*f(m)<0):
            a=m

        m=(a+b)/2
    print(m)
def f(x):
    return x**3-30*(x**2)+2552

bisection(20,0)