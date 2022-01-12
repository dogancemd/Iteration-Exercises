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