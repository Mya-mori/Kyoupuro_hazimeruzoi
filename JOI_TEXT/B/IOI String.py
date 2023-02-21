N = int(input())
S = input()

ans = 0

for i in range(N):
    if i % 2 == 0:
        if S[i] == "I":
            ans += 0
        else:
            ans += 1
    elif i % 2 == 1:
        if S[i] == "O":
            ans += 0
        else:
            ans += 1
print(ans)