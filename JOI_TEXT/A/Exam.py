A, B, C = map(int, input().split())

# A is min
if A <= B and A <= C:
    print(B + C)
# B is min
elif B <= A and B <= C:
    print(A + C)
# C is min
else:
    print(A + B)