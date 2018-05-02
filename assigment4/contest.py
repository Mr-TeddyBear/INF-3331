from numpy_integrator import numpy_midpoint_integrate
from numpy import pi, sin
import time
def f_1(x):
    return 1/pi * sin(x)/(x) * sin(x/3.)/(x/3.) * sin(x/5.)/(x/5.)

def f_2(x):
    return 1/pi * sin(x)/(x) * sin(x/3.)/(x/3.) * sin(x/5.)/(x/5.) * sin(x/7.)/(x/7.)

def f_3(x):
    return 1/pi * sin(x)/(x) * sin(x/3.)/(x/3.) * sin(x/5.)/(x/5.) * sin(x/7.)/(x/7.) * sin(x/9.)/(x/9.) * sin(x/11.)/(x/11.)

def f_4(x):
    return 1/pi * sin(x)/(x) * sin(x/3.)/(x/3.) * sin(x/5.)/(x/5.) * sin(x/7.)/(x/7.) * sin(x/9.)/(x/9.) * sin(x/11.)/(x/11.) * sin(x/13.)/(x/13.)

def f_5(x):
    return 1/pi * sin(x)/(x) * sin(x/3.)/(x/3.) * sin(x/5.)/(x/5.) * sin(x/7.)/(x/7.) * sin(x/9.)/(x/9.) * sin(x/11.)/(x/11.) * sin(x/13.)/(x/13.) * sin(x/15.)/(x/15.)

def f_6(x):
    return 1/pi * sin(x)/(x) * sin(x/4.)/(x/4.) *sin(x/4.)/(x/4.) * sin(x/7.)/(x/7.) * sin(x/7.)/(x/7.) * sin(x/9.)/(x/9.) *  sin(x/9.)/(x/9.)

N = int(1e8)
start_time = time.time()
a = numpy_midpoint_integrate(f_1,1e-20,1e7,N)
E = time.time() - start_time
print ("Integral of function %g took %f seconds. \nDiff: %e \nCalculated value: %e" % (1,E,abs(a-0.5),a))

start_time = time.time()
a = numpy_midpoint_integrate(f_2,1e-20,1e7,N)
E = time.time() - start_time
print ("Integral of function %i took %f seconds. \nDiff: %e \nCalculated value: %e" % (2,E,abs(a-0.5),a))

start_time = time.time()
a = numpy_midpoint_integrate(f_3,1e-20,1e7,N)
E = time.time() - start_time
print ("Integral of function %i took %f seconds. \nDiff: %e \nCalculated value: %e" % (3,E,abs(a-0.5),a))

start_time = time.time()
a = numpy_midpoint_integrate(f_4,1e-20,1e7,N)
E = time.time() - start_time
print ("Integral of function %i took %f seconds. \nDiff: %e \nCalculated value: %e" % (4,E,abs(a-0.5),a))

start_time = time.time()
a = numpy_midpoint_integrate(f_5,1e-20,1e7,N)
E = time.time() - start_time
print ("Integral of function %i took %f seconds. \nDiff: %e \nCalculated value: %e" % (5,E,abs(a-0.5),a))

start_time = time.time()
a = numpy_midpoint_integrate(f_6,1e-20,1e7,N)
E = time.time() - start_time
print ("Integral of function %i took %f seconds. \nDiff: %e \nCalculated value: %e" % (6,E,abs(a-0.5),a))
