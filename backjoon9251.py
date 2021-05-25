#문제 난이도 골드5
#알고리즘 종류 dp
#푼 날짜 5/24
a = str(input())
b = str(input())
lis = [[0 for i in range(len(a)+1)]for j in range(len(b)+1)]
for i in range(len(b)+1):
    for j in range(len(a)+1):
        if i == 0 or j == 0:
            ten =1 
        elif  a[j-1] == b[i-1]:
            lis[i][j] = lis[i-1][j-1]+1
        else:
            lis[i][j] = max(lis[i-1][j],lis[i][j-1])
print(lis[len(b)][len(a)])