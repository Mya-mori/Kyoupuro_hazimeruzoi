N = int(input())
K = int(input())
S = input()

k_num = 0

for i in range(N-1):
    if S[i] == "R":
        k_num += 1

if k_num == K:
    print("W")
else:
    print("R")