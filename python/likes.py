def likes(arr):
    s_end=" like"+"s"*(len(arr)<2)+" this"
    if len(arr)==0:
        stringf="no one"
    elif len(arr)==1:
        stringf=arr[0]
    elif len(arr)==2:
        stringf=arr[0]+" and "+arr[1]
    elif len(arr)==3:
        stringf=arr[0]+", "+arr[1]+" and "+arr[2]
    else:
        stringf=arr[0]+", "+arr[1]+" and "+str(len(arr)-2)+" others"
    return stringf+s_end