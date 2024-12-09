import re as regex
naughty = 0

strings = open("data.txt").read().split()

for s in strings:
    s = s.strip()
    if regex.match(r"\w*(\w\w)\w*\1\w*", s) is None:
        naughty += 1
    elif regex.match(r"\w*(\w)[^\1]\1\w*", s) is None:
        naughty +=1
        
print(len(strings)-naughty)
