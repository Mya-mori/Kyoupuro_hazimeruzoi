n = int(input()) # 移動回数
s = input() # 移動の文字列

x, y = 0, 0 # 高橋君の現在位置

visited = set() # 訪れた座標を保存するset

visited.add((x, y)) # 始点を追加

for i in range(n):
    if s[i] == "R":
        x += 1
    elif s[i] == "L":
        x -= 1
    elif s[i] == "U":
        y += 1
    elif s[i] == "D":
        y -= 1

    if (x, y) in visited: # 既に訪れたことがある座標ならばYesを出力して終了
        print("Yes")
        exit()

    visited.add((x, y)) # 訪問済みの座標を追加

print("No") # 訪れたことがある座標がなかった場合はNoを出力