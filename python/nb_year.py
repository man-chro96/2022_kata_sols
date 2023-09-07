import math
def nb_year(p0, percent, aug, p):
    i=0
    sum=p0
    while(sum < p):
        sum=sum*(1+(percent/100))+aug
        sum=math.floor(sum)
        i+=1
    return i