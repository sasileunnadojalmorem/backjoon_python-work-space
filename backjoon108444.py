dp = [[0 for i in range(0,10)]for i in range(0,101)]
for i in range(0,8):
    dp[0][i] = 2
dp[0][8] = 1
for i in range(0,101):
    dp[i] 