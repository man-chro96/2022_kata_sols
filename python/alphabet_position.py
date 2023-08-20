def alphabet_position(text):
    l=""
    text.replace(" ","")
    for i in text:
        if i.isalpha():
            l+=str(ord(i.lower())-96)+' '
    return l[:-1]