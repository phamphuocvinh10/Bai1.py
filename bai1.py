x=float(input("Enter x="))
def solution(x):
    mu=3;
    eps = 0.0001
    first = -x
    second = first-(x**2/2)
    while(abs(first-second) > eps) :
        first=second
        second=first-(x**mu/mu)
        mu=mu+1
    return first
print("solution : ",solution(x))

