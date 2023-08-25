def mean_sqaure_error(array_a, array_b):
    l=len(array_a)
    sum=0
    for i in range(l):
        sum+=(array_a[i]-array_b[i])**2
    return sum/l