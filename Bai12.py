def solution_12(x):
    mu=5;
    eps = 0.0001
    first = 2*x
    second = first+((x**3/3)*2)
    while(abs(first-second) > eps) :
        first = second
        second=first+(x**mu/mu)*2
        mu=mu+2
    return first
print("solution 12 : ",solution_12(x))
print("result 12 : ",math.log((1+x)/(1-x)))

