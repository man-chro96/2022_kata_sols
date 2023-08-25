def count_char_types(s):
    c1=0
    c2=0
    c3=0
    c4=0
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i] in alphabet.upper():
            c1+=1
        elif s[i] in alphabet:
            c2+=1
        elif s[i] in '0123456789':
            c3+=1
        else:
            c4+=1
    return [c1,c2,c3,c4]