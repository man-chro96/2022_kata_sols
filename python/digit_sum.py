#6 kyu Micro Optimization: Digit Sum
def digit_sum(n):
    s = 0
    n = str(n)
    for i in range(len(n)):
        s += int(n[i])
    return s