def solution_7(x):
    mu=4;
    eps = 0.0001
    first = 1
    second = first-(x**2/math.factorial(2))
    while(abs(first-second) > eps) :
        first = second
        if(mu % 2 ==0):
            second=first+(x**mu/math.factorial(mu))
        else:
            second = first - (x ** mu / math.factorial(mu))
            mu = mu + 2
        return first
        print("solution 7 : ", solution_7(x))
        print("result 7 : ", math.cos(x))