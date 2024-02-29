import re

word = "AbbAbc_bbab_babAc_cacVabcab_cvbdb"

pattern = re.compile(r"[A-Z]")

word = pattern.sub(" ",word)
print(word)


