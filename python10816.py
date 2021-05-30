#문제 난이도:실버2
#알고리즘 종류: 이분 탐색
#푼날짜 5/25
from bisect import bisect_left
_ = int(input())
nlis = list(map(int,input().split()))

nlis.sort()
nlis.append(10000001)
m = int(input())
mlis = list(map(int,input().split()))
smlis = list(set(mlis))
dic = {}
table = []
for i in range(len(smlis)):
    dic[smlis[i]] = 0
for i in range(len(smlis)):
    a = bisect_left(nlis,smlis[i])
    if a>=len(nlis):
        y =1
    elif nlis[a] == smlis[i]: 
        cnt = 1
        b = a+1
        while nlis[b] ==smlis[i]:
            b +=1
            cnt +=1    
        dic[smlis[i]] = cnt
    else :
        y = 1
for i in range(m):
    table.append(dic[mlis[i]])
print(*table)
