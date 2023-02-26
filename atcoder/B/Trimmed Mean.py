N = int(input())
X = sorted(map(int, input().split()))

score = sum(X)
# 上位の点数
upper = 0
for i in range(len(X)-N, len(X)):
    upper += X[i]

# 下位の点数
under  = 0
for i in range(N):
    under += X[i]

score = (score - upper - under) / (len(X) - 2 * N)
print(score)