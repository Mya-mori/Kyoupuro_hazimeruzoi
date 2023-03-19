N = int(input())
A = list(map(int, input().split()))

# Aから偶数だけを取り出す
even_list = [a for a in A if a % 2 == 0]

# 取り出した偶数を元の順番で出力する
for even_num in even_list:
    print(even_num, end=' ')
