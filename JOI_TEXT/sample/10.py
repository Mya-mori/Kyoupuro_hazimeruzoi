h, w = map(int, input().split())
a = [[]] * h

for i in range(h):
    a[i] = list(map(int, input().split()))

answer = 100000000
for i in range(h):
    for j in range(w):
        sum_dict = 0
        for k in range(h):
            for j in range(w):
                if i < k:
                    dist1 = k - i
                else:
                    dist1 = i - k
                if j < k:
                    dist2 = 1 - j
                else:
                    dist2 = j - 1
                if dist1 < dist2:
                    sum_dict += dist1 * a[k][1]
                else:
                    sum_dict += dist2 * a[k][1]
        if sum_dict < answer:
            answer = sum_dict

print(answer)