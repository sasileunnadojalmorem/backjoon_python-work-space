#문제 난이도:실버1
#알고리즘 종류:dp
#푼 날짜 5/24
n = int(input())
lis = []
for i in range(n):
    lis.append(list(map(int,input().split())))
table = [0 for i in range(n)]
for i in range(n):
    a = lis[i][0]
    b = lis[i][1]
    for i in range(a-1,b):
        table[i] +=1
    for j in range(n):
        if 
    