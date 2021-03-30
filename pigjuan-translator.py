from pypinyin import pinyin, Style
import sys

with open(sys.argv[1], "r", encoding="utf8") as f:
    s = "".join(i[0] for i in pinyin(f.read(), style=Style.FIRST_LETTER))
    print(s.upper())
