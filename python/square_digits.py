def square_digits(num):
    dig=str(num)
    l=''
    for i in dig:
        l+=str(int(i)**2)
    return int(l)