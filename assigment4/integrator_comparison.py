from numba_integrator import numba_integrate, numba_midpoint_integrate
from numpy_integrator import numpy_integrate, numpy_midpoint_integrate
from _integrator import integrate, midpoint_integrate
import numpy as np
from math import sin,pi
import time

def numpy_func(x):
    return np.sin(x)
def python_func(x):
    return sin(x)

def compare_and_time(func,method,a,b,real_answer,N):
    t0 = time.time()
    calc = method(func,a,b,N)
    t_end = time.time()
    diff = abs(calc-real_answer)
    return calc,diff,t_end-t0

methods = [integrate,midpoint_integrate,numpy_integrate,numpy_midpoint_integrate,numba_integrate,numba_midpoint_integrate]

method_str = ["Python integrator","Python midpoint integrator","NumPy integrator","NumPy midpoint integrator","Numba integrator","Numba midpoint integrator"]

results = []
expected = 2
req_N = []

for i in methods:
    N = int(1e4)
    a = [10,10,10]
    while a[1] > 1e-10:
        N = int(N)
        # print ("%1.6e" % a[1])
        # print ("N is now %e" % N)
        a = compare_and_time(numpy_func,i,0,pi,expected,N)
        N *= 1.01
    print ("Test completed")
    req_N.append(N)
    results.append(a)
for i,j,k in zip(method_str,results,req_N):
    print ("Integral of sin(x) using %s.\n  Calculated integral:                   %1.5f\n  Difference from real answer:           %.6e\n  The requierd number of itterations:    %1.6e\n  Runtime using %.0e itterations:       %2.4f seconds\n \n" % (i,j[0],j[1],k,k,j[-1]))
