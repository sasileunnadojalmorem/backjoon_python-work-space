#문제 난이도 : 실버 2
#푼 날짜:5월 24일
#알고리즘 분류:dp 단순 반복문
n = int(input())
lis = list(map(int,input().split()))
dp = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if lis[j]<lis[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))