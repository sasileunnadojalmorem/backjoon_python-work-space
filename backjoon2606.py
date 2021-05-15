N = int(input())
M = int(input())
matrix=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1
visit_list=[0 for i in range(0,N+1)]
def dfs(V):
    visit_list[V]=1 #방문한 점 1로 표시
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)
cnt = 0
dfs(1)
for i in range(1,len(visit_list)):
    if visit_list[i] == 1:
        cnt +=1
print(cnt-1)
 c6v