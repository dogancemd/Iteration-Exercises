def split(string,L):
    result=[]
    tmp=""
    for i in string:
        if i in L:
            result.append(tmp)
            tmp=""
        else:
            tmp+=i
    result.append(tmp)
    return result