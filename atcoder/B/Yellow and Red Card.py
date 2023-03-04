n, q = map(int, input().split())
cards = [[0, False] for _ in range(n)]

for _ in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        cards[event[1]-1][0] += 1
    elif event[0] == 2:
        cards[event[1]-1][1] = True
    else:
        x = event[1]
        if cards[x-1][1]:
            print('Yes')
        else:
            if cards[x-1][0] >= 2:
                print('Yes')
            else:
                print('No')