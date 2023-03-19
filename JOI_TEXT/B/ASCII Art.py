H, W = map(int, input().split())

# Aの値を行列として読み込む
A = []
for i in range(H):
    row = list(map(int, input().split()))
    A.append(row)

# Sを作成する
S = []
for i in range(H):
    s = ""
    for j in range(W):
        if A[i][j] == 0:
            s += "."
        else:
            s += chr(A[i][j] + 64)
    S.append(s)

# Sを出力する
for s in S:
    print(s)
