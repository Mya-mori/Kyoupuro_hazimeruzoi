import re

N = int(input())
S = input()
if re.fullmatch(".*I.*O.*I.*", S):
    print("Yes")
else:
    print("No")