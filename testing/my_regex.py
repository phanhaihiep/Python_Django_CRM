# chuỗi của người dùng là chữ p
# kết thúc là n
# giữa p và n chỉ được phép thêm 3 ký tự bất kỳ

string = "padddcn"
import re
from typing import Pattern
Pattern = "^p...n$"

#if string.startswith("p") and string.endswith("n") and len(string) ==5:
if re.match(Pattern, string):
    print(" Đạt yêu cầu")
else:
    print("NOK")

chuoi = "-623abc-5xyz-12k9l-2-p"
pattern2 = r"[a-zA-Z]+"
print(list(map(str, re.findall(pattern2, chuoi))))

chuoi3 = "-623abc-5xyz-12k9l-2-p"
pattern4 = r"-\s+"
print(list(map(int, re.findall(pattern4, chuoi3))))

chuoi2 = "-1212ac-vpbank-1213ac-vpbank2"
pattern3 = r"[a-zA-Z]+"
print(list(map(str, re.findall(pattern3, chuoi2)))