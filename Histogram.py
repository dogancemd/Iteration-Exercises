def histogram(L,n):
    histo=[]
    for i in range(n):
        histo.append([])
    hrange=max(L)-min(L)+1
    width=hrange/n
    for i in L:
        for index in range(n):
            if i < min(L)+(index+1)*width:
                histo[index].append(i)
                break
    return histo