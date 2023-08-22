def is_isogram(string):
    s=string.lower()
    for i in range(len(s)):
        if s[i] in s[:i]+s[i+1:]:
            return False
    return True
