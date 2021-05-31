import sys
input = sys.stdin.readline
lis = []
n = int(input())
for i in range(n):
    lis.append(int(input()))
lis.sort()
for i in lis:
    print(i)