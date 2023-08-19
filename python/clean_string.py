def clean_string(s):
  res = ""
  for i in range(len(s)):
    if s[i] == '#':
        res = res[:-1]
    else:
        res += s[i]
  return res