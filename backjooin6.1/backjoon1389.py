import sys
input = sys.stdin.readline
n,m = map(int,input().split())
mina = sys.maxsize
lis = [[mina for i in range(n)]for j in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    lis[a-1][b-1] = 1
    lis[b-1][a-1] = 1
for i in range(len(lis)):
    for j in range(len(lis)):
        for q in range(len(lis)):
            if j!= q:
                lis[j][q] = min(lis[j][i] + lis[i][q],lis[j][q])
            else:
                lis[j][q] == 1
ans = []
for i in lis:
    ans.append(sum(i))
for i in range(len(ans)):
    if ans[i] == min(ans):
        print(i+1)
        break
    