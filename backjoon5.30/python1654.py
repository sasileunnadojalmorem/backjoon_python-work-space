import sys
answer = []
k,n = map(int,input().split())
lis =  [int(sys.stdin.readline()) for _ in range(k)]
lis.sort()
a = 1
b = max(lis)
 
cnt = 0

while a<=b:
    c = (b + a)//2 
    cnt = 0 
    for i in lis:
        cnt += i//c
    if cnt >=n:
        a = c + 1    
    elif cnt < n:
        b =  c-1
    
 
print(b)

