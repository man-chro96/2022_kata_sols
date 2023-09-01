def nth_fib(n,computed={1:0,2:1}):
        if n not in computed:
            computed[n]= nth_fib(n-1)+nth_fib(n-2)
        return computed[n]