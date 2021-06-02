import sys
def factorial(n):
    q = 1
    for i in range(1,n+1):
        q = q * i
    return q
def zero(q):
    cnt = 0
    for i in range(len(q)):
        if q[i] == '0':
            cnt += 1
        elif q[i] != '0' :
            return cnt
    return cnt


input = sys.stdin.readline
s = int(input())
s = str(factorial(s))
lis = []
for i in range(len(s)):
    lis.append(s[i])
lis.reverse()
print(zero(lis))
