S = input()
a, b = map(int, input().split())

S_list = list(S)

a -= 1
b -= 1

S_list[a], S_list[b] = S_list[b], S_list[a]

ans = "".join(S_list)

print(ans)