from numba import jit
import time


def numba_integrate(f,a,b,N):
    f = jit(f)
    @jit(nopython=True)
    def intermidte(a,b,N):
        total_sum = 0
        dx = (b-a)/N
        for i in range(1,N+1):
            total_sum += f(a+(i*dx))*dx
        return total_sum
    return intermidte(a,b,N)

def numba_midpoint_integrate(f,a,b,N):
    f=jit(f)
    @jit(nopython=True)
    def helper_function(a,b,N):
        h = float(b-a)/N
        result = 0
        for i in range(N):
            result += f((a + h/2.0) + i*h)
        result *= h
        return result
    return helper_function(a,b,N)

def y(x):
    return x**2

if __name__ == "__main__":
    N = int(2**27)
    start_time = time.time()
    C = numba_integrate(y,0,1,N)
    end_time = (time.time()-start_time)
    print (C)
    print ("Python with numba time: %f seconds. With N=%.0e" %  (end_time, N))
