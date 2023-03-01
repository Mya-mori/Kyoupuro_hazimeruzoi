N, M = map(int,input().split())
d = {}
for i in range(N):
  d[i+1] = i + 1
for i in range(M):
  a, b = map(int,input().split())
  d[a] = b
for i in range(N):
  print(d[i+1])