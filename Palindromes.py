def palindromes(n):
    results=[]
    for i in range(n):
        numberbase10=str(i)
        numberbase2=str(bin(i))[2:]#binary basarken 0bxxxx diye basıyor; bu 0bden kurtarmak için
        if  numberbase10==numberbase10[::-1] and numberbase2 == numberbase2[::-1]:results.append(i)
    return results