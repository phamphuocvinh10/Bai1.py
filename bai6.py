def solution_6(x):
    mu=5;
    eps = 0.0001
    first = x
    second = first-(x**3/math.factorial(3))
    while(abs(first-second) > eps) :
        first = second
        if(mu % 2 ==1):
            second=first+(x**mu/math.factorial(mu))
        else:
            second=first-(x**mu/math.factorial(mu))
        mu=mu+2
    return first
print("solution 6 : ",solution_6(x))
print("result 6 : ",math.sin(x))