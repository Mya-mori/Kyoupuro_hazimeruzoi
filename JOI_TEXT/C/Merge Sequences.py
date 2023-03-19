n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans_a, ans_b = [0]*n, [0]*m

i, j = 0, 0
for k in range(n+m):
    if j >= m or (i < n and a[i] < b[j]):
        ans_a[i] = k+1
        i += 1
    else:
        ans_b[j] = k+1
        j += 1

print(*ans_a)
print(*ans_b)
