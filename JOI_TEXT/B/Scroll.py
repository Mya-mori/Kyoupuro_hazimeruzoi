N, K = map(int, input().split())
T = list(input())

for i in range(K-1, N):
    if ord("a") <= ord(T[i]) <= ord("z"):
        T[i] = T[i].upper()
    else:
        T[i] = T[i].lower()
print("".join(T))