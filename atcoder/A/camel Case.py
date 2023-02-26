S = list(input())

for i in range(len(S)):
    if ord("A") <= ord(S[i]) and ord(S[i]) <= ord("Z"):
        print(i+1)