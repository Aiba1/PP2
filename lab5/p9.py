import re

word = "AbbAbc_bbab_babAc_cacVabcab_cvbdb"

spaced_text = re.sub(r'(?<=[a-z])([A-Z])', r' \1', word)

print(spaced_text)
