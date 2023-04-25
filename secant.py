import math

epsilon = 1e-10


def solution(inputString, x):
    func = inputString.replace('x', "("+str(x)+")")
    return eval(func)


def secant(f, x0, x1, n):
    i = 1
    if solution(f, x0) == solution(f, x1):
        print("błąd")
        return
    while i <= n:
        x2 = x1 - (x1 - x0) * solution(f, x1) / (solution(f, x1) - solution(f, x0))
        i += 1
        if abs(solution(f, x2)) > epsilon:
            x0 = x1
            x1 = x2
    if type(x2) == complex:
        print("NaN")
    else:
        print('%.5f' % x2)


#Dobrze liczy
secant("math.tan(x)-1", math.pi / 4, math.pi / 3, 10)
secant("math.sin(x**2-x+(1/3))+(x/2)", -2, 1, 100)
secant("math.e**x-1", -2, 2, 10)
secant("math.sin((x-2)**2)+x/2", 0, 1, 1000)
secant("math.sin(x**2-x+(1/3))+(x/2)", -2, 1, 100)

#Źle liczy
secant("x**(1/3)", -1, 1, 100)

