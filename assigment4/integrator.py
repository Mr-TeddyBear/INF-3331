import matplotlib.pyplot as plt
import time

def integrate(f,a,b,N):
    dx = float(b-a)/(N)
    total_sum = 0
    for i in range(int(N)):
        total_sum += f(a + i*dx)
    return total_sum*dx

def midpoint_integrate(f,a,b,N):
    h = float(b-a)/N
    result = 0
    for i in range(N):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

"""
diff = []
for i in range(1,100):
    exact = 1/3
    est = integrate(f,0,1,i)
    diff.append((abs(exact-est)))
plt.plot([i for i in range(1,100)],diff)
plt.savefig("quadratic_error.png")
plt.axis([0,100,0,0.3])
plt.show()
"""

if __name__ == "__main__":
    def f(x):
        return x**2
    N = int(1e8)
    start_time = time.time()
    A = integrate(f,0,1,N)
    B = midpoint_integrate
    print (A)

    print ("Normal Python code time: %.5f. With N=%.0e" % (time.time()-start_time,N))
