from collections import Counter

N = int(input())
A = list(map(int,input().split()))
A.sort()

d = dict(Counter(A))

for i in d:
    if min(list(d.values())) == d[i]:
        print(i)
        exit()