N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_ans = [0] * 101
b_ans = [0] * 101

for i in range(N):
    a_ans[A[i]] += 1
for i in range(M):
    b_ans[B[i]] += 1

for i in range(1, 101):
    if (a_ans[i] > 0) and (b_ans[i] > 0):
        print(i)