V, A, B, C = map(int, input().split())

while V >= 0:
    if V - A >= 0:
        V -= A
    else:
        print("F")
        break
    if V - B >= 0:
        V -= B
    else:
        print("M")
        break
    if V - C >= 0:
        V -= C
    else:
        print("T")
        break