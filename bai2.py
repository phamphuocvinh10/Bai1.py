def solution_2(x):
    mu=2;
    eps = 0.0001
    first = 1
    plusOrMinus=3
    second = first-(2*3/2)*x
    while(abs(first-second) > eps) :
        first=second
        if(plusOrMinus % 2 != 0):
            second=first+(plusOrMinus*(plusOrMinus+1)/2)*(x**mu)
        else:
            second=first-(plusOrMinus*(plusOrMinus+1)/2)*(x**mu)
        mu=mu+1
        plusOrMinus=plusOrMinus+1
    return first
print("solution 2 : ",solution_2(x))
print("result 2 : ",1/((1+x)**3))
