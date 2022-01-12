def palindromes(n):
    results=[]
    for i in range(n):
        numberbase10=str(i)
        numberbase2=str(bin(i))[2:]
        if  numberbase10==numberbase10[::-1] and numberbase2 == numberbase2[::-1]:results.append(i)
    return results