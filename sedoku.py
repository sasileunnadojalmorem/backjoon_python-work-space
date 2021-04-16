def small(i):
    c = (i/9-1) / 3
    b = (i%9-1) / 3
    if a == b:
        if c+b == 0:
            i = 1
        elif c+b==2:
            i = 5
        elif c+b ==4:
            i = 9
    elif c > b: 
        if c + b == 1:
            i = 2
        elif c + b ==2:
            i = 3
        elif c + b == 3:
            i = 6
    elif c < b:
        if c + b == 1:
            i = 4
        elif c + b ==2:
            i = 7
        elif c + b == 3:
            i = 8
    return i 
a = list(map(int,input().split()))
row = []
ver = []
smallsedoku = []
for i in range(0,9):
    for j in range(0,9):
        row[i][j] = j
        ver[i][j] = j
        smallsedoku[i][j] = j
row  = [[i/9-1][a[i]]= true for i in a]#0을 제외하고
ver = [[i%9-1][a[i]]= true for i in a]#0을 제외하고
smallsedoku = [[small(i)][a[i]]=true for i in a]]#0을 제외하고
zerocount = []
for i in range(len(a)):
    if a[i] = 0:
        zerocount.append(i)
def sedouku(depth):
    for i in range(len(zerocount)):
            if  depth == len(zerocount):
                break
            for j in range(0,9):
                if  j == row[[zerocount[i]]/9-1][j] == ver[zerocount[i]%9-1][j] == smallsedoku[small[i]][j]:
                    continue
                    a[zerocount[i]] = j
                    row[zerocount[i]/9-1[i]][j] == ver[zerocount[i]%9-1][j] == smallsedoku[small[i]][j] = true
                    sedouku(depth+1)
                    row[zerocount[i]/9-1[i]][j] == ver[zerocount[i]%9-1][j] == smallsedoku[small[i]][j] = j
b = sedoku(0)
print(a)


