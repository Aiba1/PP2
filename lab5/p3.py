import re 

word = "Abbb___cAb_Abbcccca_bcAbcc"

pattern=re.compile(r"[a-z]+")

matches = pattern.finditer(word)

for match in matches:
    print(match)