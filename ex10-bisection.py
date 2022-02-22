# Defining Function
from math import sin
from math import cos
from numpy import log as ln,log
from datetime import date, datetime, timedelta
e = 2.71828182846
def final_answer(x):
    now = datetime.now()
    the_date = now.day * 10000 + now.hour * 100 + now.minute
    # print(the_date)
    x=float(x)
    x = str(round(x, 6)) + "00000" + str(the_date)
    return x
from decimal import Decimal
import math

def bisection(func,a, b,eps=10**-10):
    if (func(a) * func(b) > 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    i=0
    while ((b - a) >= eps):

        i+=1
        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if (-eps<func(c) <eps):
            break

        # Decide the side to repeat the steps
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    print("count : "+str(i))
    return c


def roots(f,g,factor,eps=10**-10):
    #f=function
    #eps=epsilon
    #factor=array of the segments
    #g=the derivative function
    root=[]

    for i in range(len(factor)-1):
        a=factor[i]
        print(a)
        b=factor[i+1]
        print(b)
        if a==0:
            continue

        x=f(a)
        print(x)
        y=f(b)
        print(y)

        if -eps<x<eps:
            root.append(a)

        if x*y<0:
            root.append(bisection(f,a,b,eps))

        elif g(a)*g(b)<0 :

            res=bisection(g, a, b, eps)
            if -eps<f(res)<eps:
                root.append(res)


    return root


#print(bisection(lambda x:2*x,-0.5,0.2))
p = lambda x: (x*e**(-x)+ln(x**2))*(2*x**3+2*x**2-3*x-5)
Dp = lambda x: (e**(-x) + 2/x - e**(-x)*x)*(-5 - 3 *x + 2 *x**2 + 2* x**3) + (-3 + 4 *x + 6* x**2)* (e**(-x) *x + log(x**2))
root=roots(p,Dp,[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5])
for i in root:
    print(final_answer(i))
#li=roots(lambda x:math.sin(x),lambda x:math.cos(x),[range(0,5)])
#print(li)


