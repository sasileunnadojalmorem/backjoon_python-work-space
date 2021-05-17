n = int(input())
table = [[0 for i in range(n)] for j in range(n)]
vis = [[0 for i in range(n)] for j in range(n)]
color_count = []
color = 0
for i in range(0,n):
    a = str(input())
    for j in range(n):
        table[i][j] = int(a[j])
cnt = 2
def bfs(x,y):
    global cnt 
    global color
    vis[y][x] = 1
    table[y][x] = cnt
    dxx = [-1,0,1,0]
    dyy = [0,-1,0,1]
    color +=1
    for i in range(0,4):
        dx = dxx[i] + x
        dy = dyy[i] + y
        if  dx>=0 and dx<n and dy>=0 and dy<n:
            if vis[dy][dx] == 0 and table[dy][dx] == 1 :
                bfs(dx,dy)
        
    return
for i in range(0,n):
    for j in range(0,n):
        if table[i][j] == 1:
            bfs(j,i)
            color_count.append(color)
            cnt +=1
            color = 0
color_count.sort()
print(len(color_count))
for i in range(0,len(color_count)):
    print(color_count[i])

