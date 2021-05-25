n = int(input())
lis = list(map(int,input().split()))
dp = [0 for i in range(n)]
dp[0] = lis[0]
for i in range(1,n):
    dp[i] = max(dp[i-1]+lis[i],lis[i])
print(max(dp))