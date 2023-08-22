def next_pal(val):
    while True:
        val+=1
        if val==int(str(val)[::-1]):
            break
    return val