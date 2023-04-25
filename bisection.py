import math

epsilon = 1e-10


def solution(inputString, x):
    func = inputString.replace('x', "(" + str(x) + ")")
    return eval(func)


def bisection(f, a, b, n):
    i = 0
    c = (a + b) / 2
    while abs(solution(f, c)) > epsilon and i < n:
        if solution(f, c) * solution(f, a) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        i += 1
    if type(c) == complex:
        print("NaN")
    else:
        print('%.5f' % c)


# W metodzie bisekcji nie ma problemu ze znalezieniem pierwiastka funkcji ponieważ nigdy nie zajdzie np. dzielenie przez 0.
# Problematyczne może być szukanie miejsca zerowego na małym przedziale
bisection("x**(1/3)", -1, 1, 1000)
bisection("math.tan(x)-1", -math.pi / 2, math.pi / 2, 10)
bisection("math.sin(x**2-x+(1/3))+(x/2)", -2, 1, 100)


#Przykłady dodatkowe
# bisection("x-2", -10, 10, 100)
# bisection("math.log(x)", 0.1, 10, 10)
# bisection("x**2-4", -5, 5, 10)
# bisection("math.sin(x)", math.pi, 2 * math.pi, 10)
