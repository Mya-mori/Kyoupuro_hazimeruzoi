A, B, C = map(int, input().split())

# A is middle
if (B <= A and A <= C) or (C <= A and A <= B):
    print(A)
# B is middle
elif (A <= B and B <= C) or (C <= B and B <= A):
    print(B)
# C is min
else:
    print(C)