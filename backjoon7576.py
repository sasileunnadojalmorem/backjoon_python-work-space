from collections import deque
n,m = map(int,input().split())
one_list = []
table = [list(map(int,input().split())) for j in range(m)]
vis = [[0 for i in range(n)]for j in range(m)]
fcnt = 0

for row in table:
    if 0 in row:
        fcnt += row.count(0)
for i in range(m):
    for j in range(n):
        if table[i][j] == 1:
            one_list.append([j,i])
def bfs(list):
    queue = deque()
    for i in range(len(list)):
        a = list[i][0]
        b = list[i][1]
        vis[b][a] = 1
        queue.append(a)
        queue.append(b)
    while queue:
        qx = queue.popleft()
        qy = queue.popleft()
        dxx = [-1,0,1,0]
        dyy = [0,-1,0,1]
        for i in range(0,4):
            dx = qx + dxx[i]
            dy = qy + dyy[i]
            if dx>=0 and dx<n and dy>=0 and dy<m :
                if vis[dy][dx] == 0 and table[dy][dx] == 0:
                    vis[dy][dx] = 1
                    table[dy][dx] = table[qy][qx] + 1
                    queue.append(dx)
                    queue.append(dy)   
bfs(one_list)
maxa = 0
cnt = 0
for row in table:
    if 0 in row:
        cnt += row.count(0)
    maxb = max(row)
    maxa = max(maxb,maxa)
if fcnt ==0:
    print(0)
elif cnt>0:
    print(-1)
else :
    print(maxa-1) 





