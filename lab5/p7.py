import re

word = "bbbc_bbab_babc_cacabcab_cvbdb"

word = word.split("_")
word = "".join(words.capitalize() for words in word[1:])
print(word)
