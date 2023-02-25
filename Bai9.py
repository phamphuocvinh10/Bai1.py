def solution_9(x):
    mu=4;
    eps = 0.0001
    first = 1
    second = first-(x**2/math.factorial(3))
    while(abs(first-second) > eps) :
        first = second
        if(mu % 2 ==0):
            second=first+(x**mu/math.factorial(mu+1))
        else:
            second=first-(x**mu/math.factorial(mu+1))
        mu=mu+2
    return first
print("solution 9 : ",solution_9(x))
print("result 9 : ",(math.sin(x)/x))
