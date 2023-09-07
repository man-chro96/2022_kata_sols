def multiples3_5(n):
    sum=0
    if n <=0:
        return 0
    else:
        for i in range(n-1,0,-1):
            if i % 3 ==0 or i % 5 ==0:
                sum=sum+i
        return sum