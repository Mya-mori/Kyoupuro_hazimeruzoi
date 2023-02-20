import math
S = int(input()) #目標の高さ
A = int(input()) #ベース
B = int(input()) #追加分

if S - A > 0:
    diff = S - A
else:
    diff = 0

add_ice = math.ceil(diff / B)
print(250 + (add_ice * 100))