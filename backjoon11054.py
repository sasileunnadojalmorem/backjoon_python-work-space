#문제 난이도:골드3
#알고리즘 분류:dp
#푼 날짜 :5/24
n = int(input())
lis = list(map(int,input().split()))
dp = [1 for i in range(n)]
olis = list(reversed(lis))
odp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if lis[j]<lis[i]:
            dp[i] = max(dp[i],dp[j]+1)
for i in range(n):
    for j in range(i):
        if olis[j]<olis[i]:
            odp[i] = max(odp[i],odp[j]+1)
odp = list(reversed(odp))
for i in range(n):
    dp[i] = dp[i]+ odp[i]
print(max(dp))

