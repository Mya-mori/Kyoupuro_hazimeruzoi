n,a,b = map(int,input().split())
s = input()

answer = s[:a-1]
for i in range(b-a+1):
    answer += s[b-1-i]
answer += s[b:]
print(answer)