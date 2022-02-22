# Simpson's 1/3 Rule
# Define function to integrate
from math import sin
from datetime import date, datetime, timedelta
def final_answer(x):
    now = datetime.now()
    the_date = now.day * 10000 + now.hour * 100 + now.minute
    # print(the_date)
    x=float(x)
    x = str(round(x, 6)) + "00000" + str(the_date)
    return x
from numpy import log as ln
e = 2.71828182846
def f(x):
    return (x*e**(-x)+ln(x**2))*(2*x**3+2*x**2-3*x-5)



# Implementing Simpson's 1/3
def simpson13(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n
    print(h)

    # Finding sum
    print(f(x0))
    integration = f(x0) + f(xn)

    for i in range(1, n):

        k = x0 + i * h
        print(k)
        print(f(k))


        if i % 2 == 0:
            print(str(integration)+"+ 2 *"+str(f(k))+"=")
            integration = integration + 2 * f(k)
            print(integration)
        else:
            print(str(integration) + "+ 4 *" + str(f(k)) + "=")
            integration = integration + 4 * f(k)
            print(integration)


    # Finding final integration value
    integration = integration * h / 3

    return integration


# Call trapezoidal() method and get result
result = simpson13(0.5, 1, 4)
print("Integration result by Simpson's 1/3 method is: " , (final_answer(result)))