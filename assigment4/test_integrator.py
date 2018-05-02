from numba_integrator import numba_integrate, numba_midpoint_integrate
from numpy_integrator import numpy_integrate, numpy_midpoint_integrate
from _integrator import integrate, midpoint_integrate
import time

def test_integral_of_constat_function():
    def f(x):
        return 2
    def compare_and_time(func,method,a,b,real_answer,N):
        t0 = time.time()
        calc = method(func,a,b,N)
        t_end = time.time()
        diff = abs(calc-real_answer)
        return calc,diff,t_end-t0

    method_str = ["Python integrator","Python midpoint integrator","NumPy integrator","NumPy midpoint integrator","Numba integrator","Numba midpoint integrator"]

    methods = [integrate,midpoint_integrate,numpy_integrate,numpy_midpoint_integrate,numba_integrate,numba_midpoint_integrate]

    N = 1000
    tol = 1/N

    for i,j in zip(methods,method_str):
        a,b,c = compare_and_time(f,i,0,1,2,N)
        assert (b <= tol), "Test of %s metohd failed, Diff: %1.6e" % (j,b)
    print ("All constant function integrations where completed correctly.")

def test_of_linear_function():
    def f(x):
        return 2*x
    def compare_and_time(func,method,a,b,real_answer,N):
        t0 = time.time()
        calc = method(func,a,b,N)
        t_end = time.time()
        diff = abs(calc-real_answer)
        return calc,diff,t_end-t0

    method_str = ["Python integrator","Python midpoint integrator","NumPy integrator","NumPy midpoint integrator","Numba integrator","Numba midpoint integrator"]

    methods = [integrate,midpoint_integrate,numpy_integrate,numpy_midpoint_integrate,numba_integrate,numba_midpoint_integrate]

    N = 10000
    tol = 1.1/(N)

    for i,j in zip(methods,method_str):
        a,b,c = compare_and_time(f,i,0,1,1,N)
        assert (b <= tol), "Test of %s metohd failed, Diff: %1.6e" % (j,b)

    print ("All linear function integrals completed correctly.")


def timings():
    N = int(1e7)
    def a(x):
        return x**2

    start_time = time.time()
    C = numba_integrate(a,0,1,N)
    E = time.time()-start_time
    print ("Python with numba time: %f seconds. With N=%.0e" %  (E, N))

    start_time_ = time.time()
    A = integrate(a,0,1,N)
    E = time.time()-start_time
    print ("Normal Python code time: %.5f. With N=%.0e" % (E,N))

    start_time = time.time()
    B = numpy_integrate(a,0,1,N)
    E = time.time()-start_time
    print ("Numpy code time: %f seconds. With N=%.0e" %  (E, N))

test_integral_of_constat_function()
test_of_linear_function()
timings()
