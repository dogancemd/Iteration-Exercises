def perfect_numbers(n):
    results=[[],[],[]]
    for num in range(1,n):
        dividers=[]
        for divider in range(1,num):
            if num % divider == 0:
                dividers.append(divider)
        sums=sum(dividers)
        if sums==num:
            results[0].append(num)
        elif sums>num:
            results[1].append(num)
        else:
            results[2].append(num)
    return tuple(results)