def lis(L):
    number1=1
    number2=1
    for i in range(len(L)-1):
        if L[i]<=L[i+1]:
            number2+=1
        else:
            if number1<number2:
                number1=number2
            number2=1
    return max(number1,number2)