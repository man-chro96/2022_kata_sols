def args_count(*args,**kwargs):
    sum=0
    for i in args:
        sum+=1
    for j in kwargs:
        sum+=1
    return sum