def max3N1P(n):
    def the3N1P(n):
        seq = []
        while True:
            if n==1:
                seq.append(1)
                return len(seq)
            elif n%2==1:
                n=3*n+1
                seq.append(n)
            else:
                n=n/2
                seq.append(n)
    results=[0]
    for i in range(1,n):
        results.append(the3N1P(i))
    maximum=max(results)
    return(results.index(maximum),maximum)