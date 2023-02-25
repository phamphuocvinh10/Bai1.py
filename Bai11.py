def solution_11(x):
    mu=3;
    eps = 0.0001
    first = x
    second = first-(x**2/2)
    while(abs(first-second) > eps) :
        first = second
        if(mu % 2 ==1):
            second=first+(x**mu/mu)
        else:
            second=first-(x**mu/mu)
        mu=mu+1
    return first
print("solution 11 : ",solution_11(x))
print("result 11 : ",math.log(1+x))