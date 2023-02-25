def solution_3(x):
    mu=3;
    eps = 0.0001
    first = -x
    second = first-(x**2/2)
    while(abs(first-second) > eps) :
        first=second
        second=first-(x**mu/mu)
        mu=mu+1
    return first
print("solution 3 : ",solution_3(x))
print("result 3 : ",math.log(1-x))