from math import sin
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

def newtonRaphson(f,g,x0, e=10**-10, N=21):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
        return x1
    else:
        print('\nNot Convergent.')

def roots(f,g,factor,eps=10**-10):
    #f=function
    #eps=epsilon
    #factor=array of the segments
    #g=the derivative function
    flag =0
    root=[]

    for i in range(len(factor)-1):
        a=factor[i]
        b=factor[i+1]
        if a == 0:
            continue

        x=f(a)
        y=f(b)

        if -eps<x<eps:
            root.append(a)
            continue

        if x*y<0:
            root.append(newtonRaphson(f,g,(a+b)/2))
            res=newtonRaphson(f,g,(a+b)/2)
            if res:
                for i in root:
                    a = round(i, 7)
                    b = round(res, 7)
                    if a == b:
                        flag = 1
                if flag:
                    continue
            continue


        elif g(a)*g(b)<0 :

            res=newtonRaphson(f,g,(a+b)/2)
            if res:
                for i in root:
                    a = round(i, 7)
                    b = round(res, 7)
                    if a == b:
                        flag = 1
                if flag:
                    continue

                if -eps<f(res)<eps:
                    root.append(res)
            else:
                continue


    return root

p = lambda x: (x*e**(-x)+ln(x**2))*(2*x**3+2*x**2-3*x-5)
Dp = lambda x: (e**(-x) + 2/x - e**(-x)*x)*(-5 - 3 *x + 2 *x**2 + 2* x**3) + (-3 + 4 *x + 6* x**2)* (e**(-x) *x + log(x**2))
approx=roots(p,Dp,[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5])
for i in approx:
    print(final_answer(i))
print(approx)