def solution_5(x):
    mu=2;
    eps = 0.0001
    first = 1
    second = first-((1/2)*x)
    sumchan=2
    sumle=1
    biendemle=3
    biendemchan=4
    while (abs(first - second) > eps):
        first = second
        sumle = sumle * biendemle
        sumchan = sumchan * biendemchan
        if (mu % 2 == 0):
            second = first + ((sumle/sumchan)*(x**mu))
        else:
            second = first - ((sumle / sumchan) * (x ** mu))
        mu = mu + 1
        biendemchan=biendemchan+2
        biendemle=biendemle+2
    return first
print("solution 5 : ",solution_5(x))
print("result 5 : ",1/(math.sqrt(1+x)))