from collections import deque
n = int(input())
for i in range(n):
    _,b = map(int,input().split())
    queue = list(map(int,input().split()))
    q =deque()
    cnt = 1
    for i in range(len(queue)):
        q.append([queue[i],i])
    while len(q) > 0:
        if q[0][0] != max(queue):
            c = q.popleft()
            q.append(c)
        elif q[0][0] == max(queue):
            if  q[0][1] == b:
                print(cnt)
                break
            else:
                cnt +=1
            q.popleft()
            queue.remove(max(queue))
            
