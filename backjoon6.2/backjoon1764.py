import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lis = []
answer = []
for i in range(n):
    n = str(input()).rstrip()
    lis.append(n)
for i in range(m):
    n = str(input()).rstrip()
    answer.append(n)
answer = list(set(lis) & set(answer))
print(len(answer))
for i in sorted(answer):
    print(i)

    