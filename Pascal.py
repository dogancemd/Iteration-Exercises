def fact(n):
    result=1
    if n == 0:
        return 1
    for i in range(1,n+1):
        result*=i
    return result
def comb(num1,num2):
    return (fact(num1))/(fact(num1-num2)*fact(num2))
def pascal(n):
    def fact(n):
        result=1
        if n == 0:
            return 1
        for i in range(1,n+1):
            result*=i
        return result
    def comb(num1,num2):
        return (fact(num1))/(fact(num1-num2)*fact(num2))
    result=[]
    for i in range(n):
        row=[]
        for a in range(i+1):
            row.append(int(comb(i,a)))
        result.append(row)
    return result