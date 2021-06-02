import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic = {}
for i in range(n):
    a = input().rstrip()
    dic[a] = i+1
    dic[f'{i+1}'] = a
for i in range(m):
    q = input().rstrip()
    print(dic[q])
    
