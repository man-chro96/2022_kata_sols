import itertools
def longest_repetition(chars):
    if chars=='':
        return ('',0)
    arr=[]
    for x,y in itertools.groupby(chars):
         arr.append(''.join(y))
    max=len(arr[0])
    maxi=arr[0][0]
    for i in range(len(arr)):
        if len(arr[i])>max:
            max=len(arr[i])
            maxi=arr[i][0]
    return(maxi,max)
