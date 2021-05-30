from collections import deque
n,m = map(int,input().split())
lis = [list(map(int,input().split())]for j in range(n)]
vis = [[0 for i in range(m)]for j in range(n)]
def bfs(x,y,0):
  queue = deque([])
  vis[y][x] = 1
  queue.append(x)
  queue.append(y)
  while queue:
    qx = queue.left
    qy = queue.leftpop()
    ddx = [-1,0,1,0]
    ddy = [0,-1,0,1]
    for i in range(0,4):
      ddx = qx + ddx[i]
      ddy = qy + ddy[i]
      if ddx>=0 and ddx>m and ddy>=0 and ddy>n:
        if vis[ddy][ddx] == 0 and lis[ddy][ddx] == 1:
          queue.append(ddx)
          queue.append(ddy)
          vis[ddy][ddx] = 1
          lis[ddy][ddx] = lis[qy][qx] + 1