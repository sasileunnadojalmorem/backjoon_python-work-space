from collections import deque
def bfs(x,y,cnt):
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
            if  dx>=0 and dx<xx and dy>=0 and dy<yy:
                if vis[dy][dx] == 0 and table[dy][dx] == 1 :
                    queue.append(dx)
                    queue.append(dy)
                    table[dy][dx] = cnt
                    vis[dy][dx] = 1
n = int(input())
for q in range(0,n):
    cnt = 2
    xx,yy,count = map(int,input().split())
    table = [[0 for i in range(xx)] for j in range(yy)]
    vis = [[0 for i in range(xx)] for j in range(yy)]
    for i in range(count):
        a,b = map(int,input().split())
        table[b][a] = 1
    for i in range(0,yy):
        for j in range(0,xx):
            if table[i][j] == 1 and vis[i][j] == 0  :
                bfs(j,i,cnt)
                cnt +=1
    print(cnt-2)
