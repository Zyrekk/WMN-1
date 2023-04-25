import math

epsilon = 1e-10


def solution(inputString, x):
    func = inputString.replace('x', "(" + str(x) + ")")
    return eval(func)


def halley_method(f, df, dff, x0, n):
    for _ in range(1, n):
        fx = solution(f, x0)
        dfx = solution(df, x0)
        ddfx = solution(dff, x0)
        x2 = -2 * fx * dfx / (2 * dfx ** 2 - fx * ddfx)
        x0 = x0 + x2
        if abs(x2) < epsilon:
            break
    if type(x0) == complex:
        print("NaN")
    else:
        print('%.5f' % x0)


#Działa ale musi być duża dokładność
halley_method("math.sin(x**2-x+(1/3))+(x/2)",'(2*x-1)*math.cos(x**2-x+(1/3))+(1/2)','2*math.cos(x**2-x+1/3)-(2*x-1)**2*math.sin(x**2-x+1/3)', -1, 10)
halley_method('2*x**3-2*x-5', '6*x**2 - 2', '12*x', 0.5, 10)
halley_method('math.sinh(x)', 'math.cosh(x)', 'math.sinh(x)', 5, 10)

#W tym przypadku juz nie działa
halley_method("math.sin(x**2-x+(1/3))+(x/2)",'(2*x-1)*math.cos(x**2-x+(1/3))+(1/2)','2*math.cos(x**2-x+1/3)-(2*x-1)**2*math.sin(x**2-x+1/3)', -2, 10)
