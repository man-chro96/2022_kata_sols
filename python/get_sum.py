def get_sum(a,b):
    y=1*(a<=b)+-1*(a>b)
    return sum([x for x in range(a,b+y,y)])