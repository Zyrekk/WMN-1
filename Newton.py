import math

epsilon = 1e-10


def solution(inputString, x):
    func = inputString.replace('x', "(" + str(x) + ")")
    return eval(func)


def raphson(f, df, a, n):
    for i in range(n):
        if abs(solution(df, a)) < epsilon:
            break
        x1 = a - solution(f, a) / solution(df, a)
        if abs(x1 - a) <= epsilon:
            if type(x1) == complex:
                print("NaN")
            else:
                print('%.5f' % x1)
            return
        a = x1
    if type(x1) == complex:
        print("NaN")
    else:
        print('%.5f' % x1)




#Dobrze liczy
raphson('math.log(x)', '1/x', 1, 10)
raphson('math.sinh(x)', 'math.cosh(x)', -2, 99)
raphson("x**3 - x**2 + 2",'3*x**2-2*x', -1, 1000)

#Źle liczy
raphson("x**(1/3)", '1/3*x**(2/3)', -1, 100)
raphson("math.sin(x**2-x+(1/3))+(x/2)",'(2*x-1)*math.cos(x**2-x+(1/3))+(1/2)', -2, 10)
