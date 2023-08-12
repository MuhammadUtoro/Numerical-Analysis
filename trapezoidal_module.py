# Comparing trapezoid method (numerical analysis) and exact or analytical method. Taken from:
# Lingen and Langtangen - Programming for Computations with Python from Lingen and Langtangen

def trapezoidal(f,a,b,n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1,n):
        result += f(a + i*h)
    result *= h
    return result

def application():
    import math
    # This is the numerical method
    v = lambda t: 3*(t**2)*math.exp(t**3)
    n = int(input('n: '))
    num_sol = trapezoidal(v,0,1,n)
    print(num_sol)

    # This is the analytical method
    r = lambda t1: math.exp(t1**3)
    exc_sol = r(1) - r(0)
    print(exc_sol)

    # Calculating the error between analytical vs numerical
    print(exc_sol-num_sol)

if __name__ == '__main__':
    application()
