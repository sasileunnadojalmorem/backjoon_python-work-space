n = int(input())
ns = [list(map(int,input().split())) for i in range(0,n)]
dp = [0 for i in range(0,n)]
for i in range(0,n):
    dp[i] = [1 for q in range(0,i+1)]
dp[0][0] = ns[0][0]
for i in range(1,n):
    for j in range(0,len(dp[i])):
        if j-1<0:
            dp[i][j] = dp[i-1][j] + ns[i][j]
        elif j > i-1:
            dp[i][j] = dp[i-1][j-1] + ns[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + ns[i][j]
print(max(dp[n-1]))

