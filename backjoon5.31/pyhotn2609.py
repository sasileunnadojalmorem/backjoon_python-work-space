import sys
input = sys.stdin.readline
def sumsum(n):
    lis = []
    for i in range(1,int((n**0.5))+1):
        if n%i == 0:
            q = n//i
            lis.append(i)
            lis.append(q)
    lis = list(set(lis))
    return lis
n,m = map(int,input().split())
a,b =n,m
n = sumsum(n)
m = sumsum(m)
lenn = len(n)
lenm = len(m)
answer=[]
if lenn>lenm:
    for i in range(lenm):
        if m[i] in n:
            answer.append(m[i])
else:
    for i in range(lenn):
        if n[i] in m:
            answer.append(n[i])

c = max(answer)
print(c)
print(c*(a//c)*(b//c))