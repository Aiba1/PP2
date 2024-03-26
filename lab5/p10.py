import re

word = "AbbAbc_bbab_babAc_cacVabcab_cvbdb"

snake_text = re.sub(r'(?<=[a-z])([A-Z])', r'_\1', word)

print(snake_text)
