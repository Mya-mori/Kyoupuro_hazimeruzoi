N = int(input())
S = input()

string_list = []

for i in range(N):
    if S[i] not in string_list:
        string_list.append(S[i])

if len(string_list) > 2:
    print("Yes")
else:
    print("No")