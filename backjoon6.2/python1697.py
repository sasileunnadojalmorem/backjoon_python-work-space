import sys
from collections import deque
input = sys.stdin.readline
q,m = map(int,input().split())
lis = [0 for i in range(0,100001)]
queue = deque()
def bfs(n):
    queue.append(n)
    while queue:
        a = queue.popleft()
        if a == m:
            return lis[a]
        for next in (a-1,a+1,a*2):
            if 0 <= next < len(lis) and not lis[next]:
                lis[next] = lis[a] + 1
                queue.append(next)
print(bfs(q))



    