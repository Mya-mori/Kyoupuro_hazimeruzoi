N, M = map(int, input().split())
Boxes = list(map(int, input().split()))
Keys = list(map(int, input().split()))

key = list(set(Keys))

ans = 0
for i in range(len(key)):
    for j in range(len(Boxes)):
        if key[i] == Boxes[j]:
            ans += 1

print(ans)