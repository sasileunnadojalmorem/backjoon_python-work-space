n = int(input())
glass = [int(input()) for i in range(n)]
dp = [[ 0 for i in range(0,2)]for j in range(0,n)]
maxb = 0
dp[0][0] = glass[0]
dp[0][1] = glass[0]
if n >1:
    dp[1][0] = glass[1]
    dp[1][1] = glass[0] + glass[1]
    for i in range(2,n):
        dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + glass[i]
        dp[i][1] = dp[i-1][0] + glass[i] 
    for row in dp:
        maxa = max(row)
        maxb = max(maxb,maxa)
    print(maxb)
else :
    print(glass[0])
