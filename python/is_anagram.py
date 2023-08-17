def is_anagram(a, b):
    return ''.join(sorted(a.lower()))==''.join(sorted(b.lower()))