import re

word = "bbbcAbAbbccccabcAbb"

pattern = re.compile(r"[A-Za-z]+[a][A-Za-z]*[b]")

matches = pattern.finditer(word)

for match in matches:
    print(match.group(0))
