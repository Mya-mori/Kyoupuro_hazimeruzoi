from collections import Counter

N = int(input())
A = list(map(int,input().split()))
A.sort()

d = dict(Counter(A))
for i in d:
    if min(list(d.values())) == d[i]:
        print(i)
        exit()

'''
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

print(l.count('a'))
# 4

print(l.count('b'))
# 1

d = dict(k1=1, k2=2, k3=3)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}
'''