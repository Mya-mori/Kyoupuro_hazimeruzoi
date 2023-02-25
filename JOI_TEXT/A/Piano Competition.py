N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += A[i]

ans -= max(A)
ans -= min(A)

print(ans)