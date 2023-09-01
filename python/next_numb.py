def hasmult(n):
    x=str(n)
    for i in range(len(x)):
        if x[i] in x[:i]+x[i+1:]:
            return True
    return False


def next_numb(val):
    while(True):
        if val ==9999999999:
            return "There is no possible number that fulfills those requirements"
        val+=1
        if (val % 2 !=0 and val /3==int(val/3) and (not(hasmult(val)))):
            return val
