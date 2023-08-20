def stray(arr):
    return abs(sum(arr)-(len(arr)-1)*arr[-2])