N = int(input())
S = input()

x = 0
y = 0
z = 0

for i in range(N):
    if S[i] == "J":
        x += 1
    elif S[i] == "O":
        y += 1
    elif S[i] == "I":
        z += 1

ans = "J" * x + "O" * y + "I" * z

print(ans)