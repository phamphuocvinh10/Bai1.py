def solution_13_1(x):
    result = ((solution_1(x))-(1/solution_1(x)))/2
    return result
print("solution 13_1 : ",solution_13_1(x))
print("result 13_1 : ",math.sinh(x))

def solution_13_2(x):
    mu=5;
    eps = 0.0001
    first = x
    second = first+(x**3/math.factorial(3))
    while(abs(first-second) > eps) :
        first = second
        second=first+(x**mu/math.factorial(mu))
        mu=mu+2
    return first
print("solution 13_2 : ",solution_13_2(x))
print("result 13_2 : ",math.sinh(x))
