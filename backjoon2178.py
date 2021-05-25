from collections import deque
def bfs(x,y):
    cnt = 1
    queue = deque([x,y])
    vis[y][x] = 1
    table[y][x] = cnt
    while queue:
        qx = queue.popleft()
        qy = queue.popleft()
        
        dxx = [-1,0,1,0]
        dyy = [0,-1,0,1]
        for i in range(0,4):
            dx = dxx[i] + qx
            dy = dyy[i] + qy
            if dx>=0 and dx<m and dy>=0 and dy<n:
                if vis[dy][dx] == 0 and table[dy][dx] == 1:
                    vis[dy][dx] = 1
                    table[dy][dx] = table[dy - dyy[i]][dx - dxx[i]] + 1

                    queue.append(dx)
                    queue.append(dy)
n,m = map(int,input().split())
vis = [[0 for i in range(m)]for j in range(n)]
table = [[0 for i in range(m)]for j in range(n)]
for i in range(0,n):
    q = str(input())
    for j in range(m):
        table[i][j] = int(q[j])
bfs(0,0)
print(table[n-1][m-1])


                    