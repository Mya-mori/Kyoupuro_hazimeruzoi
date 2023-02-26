n = int(input())
a = list(map(int,input().split()))
x = 0
for i in range(n):
  if a[x] < a[i]:
    x  = i
answer1 = 0
for i in range(x):
  answer1 += a[i]
answer2 = 0
for i in range(x+1,n):
  answer2 += a[i]
print(answer1)
print(answer2)