dp = [0 for i in range(100)] #테이블
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2 
#점화식
for i in range(5,100):
    dp[i] = dp[i-5] + dp[i-1]
testcase = int(input())
for i in range(testcase):
    n= int(input())
    print(dp[n-1])