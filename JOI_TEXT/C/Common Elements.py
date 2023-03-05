N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = list(set(sorted(A)))
B = list(set(sorted(B)))

ans = 0

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            print(A[i])