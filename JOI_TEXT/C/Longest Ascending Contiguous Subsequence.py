N = int(input())
A = list(map(int, input().split()))

ans = []
cnt = 0

for i in range(N):
    if i == N - 1:
        break
    if A[i] <= A[i+1]:
        cnt += 1
    if A[i] > A[i+1]:
        ans.append(cnt+1)
        cnt = 0

print(max(ans))