def solution(n):
    s = ''

    def format(r, x, y, z):
        arr = ['', x, 2 * x, 3 * x, x + y, y, y + x, y + 2 * x, y + 3 * x, x + z]
        s = arr[int(n / r)]
        return s

    if n >= 1000:
        s += 'M' * (int(n / 1000))
        n = int(str(n)[1:])
    if n >= 100:
        s += format(100,'C','D','M')
        n = int(str(n)[1:])
    if n >= 10:
        s += format(10,'X','L','C')
        n = int(str(n)[1:])
        
    s += format(1,'I','V','X')
    return s