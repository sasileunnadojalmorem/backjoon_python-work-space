from bisect import bisect_left
n = int(input())
lis = list(map(int,input().split()))
lis.sort()
m = int(input())
mlis = list(map(int,input().split()))
for i in range(m):
    a = bisect_left(lis,mlis[i])
    if a>=len(lis):
        print(0)
    elif lis[a] == mlis[i]:
        print(1)
    else:
        print(0)