def f(n):
    # 数列の規則
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1
 
if __name__ == "__main__":
    s = int(input())
 
    a = s
    arr = [s]
    for i in range(1000000): # m < 1000000となるので
        a = f(a)
        if a in arr:
            # 同じ数値が現れたた出力
            print(len(arr) + 1)
            break
        # 数列の格納
        arr.append(a)