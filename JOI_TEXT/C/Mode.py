N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * 101

for i in range(N):
    cnt[A[i]] += 1

ans = 0
for i in range(101):
    if cnt[i] > ans:
        ans = cnt[i]

print(ans)