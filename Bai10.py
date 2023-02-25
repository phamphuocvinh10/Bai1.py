def solution_10(x):
    mu=5;
    eps = 0.0001
    first = x
    second = first-(x**3/3)
    while(abs(first-second) > eps) :
        first = second
        if(mu % 2 ==1):
            second=first+(x**mu/mu)
        else:
            second=first-(x**mu/mu)
        mu=mu+2
    return first
print("solution 10 : ",solution_10(x))
print("result 10 : ",math.atan(x))