def consonant_count(s):
    sum=0
    for i in s:
        if i in 'aeiuoAEIUO' or not i.isalpha():
            sum+=1
    return len(s)-sum