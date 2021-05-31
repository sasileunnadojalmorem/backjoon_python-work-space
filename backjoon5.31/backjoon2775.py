import sys
input = sys.stdin.readline
t = int(input())
dp = [[i for i in range(0,15)]for j in range(0,15)]
for i in range(1,15):
    for j in range(1,15):
        if j == 1:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
        
 
for i in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])
