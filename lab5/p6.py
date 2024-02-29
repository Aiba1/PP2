import re

word = "bbbc,Ab.AbbccccabcAbb"

pattern = re.compile(r"[,. ]+")

word = pattern.sub(":", word)
print(word)
