A, B, C = map(int, input().split())

sum = 0
count = 0

while sum < C:
    count += 1
    sum += A
    if count % 7 == 0:
        sum += B

print(count)