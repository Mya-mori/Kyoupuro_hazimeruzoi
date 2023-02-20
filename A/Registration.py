S = input()
T = input()

if S ==  T[:-1] and len(S) + 1 == len(T):
    print("Yes")
else:
    print("No")