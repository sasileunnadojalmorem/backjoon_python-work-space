import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lis = list(map(int,input().split()))
start = 1
end = max(lis)
while start <= end: 
    mid = (start + end)//2
    cnt = 0
    for i in lis:
        if i>=mid:
            cnt += i-mid
    if cnt >= m:
        start = mid + 1
    else :
        end = mid-1
print(end)
    