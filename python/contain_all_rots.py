def contain_all_rots(string: str, arr: list) -> bool:
    for i in range(len(string)):
        if string[i:] + string[:i] not in arr:
            return False
    return True

def contain_all_rots_2(strng, arr):
    arr0 = []
    for i in range(0,len(strng)):
        arr0.append(strng[i:len(strng)] + strng[0:i])
    for _ in arr0:
        if _ not in arr:
            return False
    return True