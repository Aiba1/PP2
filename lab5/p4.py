import re 

word = "AbbbcAbAbbccccabcAbb"

pattern=re.compile(r"[A-Z][a-z]+")

matches = pattern.finditer(word)

for match in matches:
    print(match)