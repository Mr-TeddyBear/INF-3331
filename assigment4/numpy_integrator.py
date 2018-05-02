import numpy as np
import time

"""
Integration using end point method and numpy
"""
def numpy_integrate(f,a,b,N):
    A = np.linspace(a,b,N,endpoint=False)
    dx = (b-a)/N
    try:
        E = f(A)[:]
    except TypeError:
        f = np.vectorize(f)
        E = dx*f(A)
    return np.sum(E)*dx

def numpy_midpoint_integrate(f,a,b,N):
    dx = float(b-a)/(N)
    A = np.linspace(a,b,N,endpoint=False)+dx/2
    try:
        E = dx*f(A)[:]
    except TypeError:
        f = np.vectorize(f)
        E = dx*f(A)
    return np.sum(E)


if __name__ == "__main__":
    def f(x):
        return x**2
    start_time = time.time()
    B = numpy_integrate(f,0,1,N)
    end_time = (time.time()-start_time)
    print ("Numpy code time: %f seconds. With N=%.0e" %  (end_time, N))
