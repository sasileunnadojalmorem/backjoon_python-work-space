def small(i):
    a = (i/9-1) / 3
    b = (i%9-1) / 3
    if a == b:
        if a+b == 0:
            i = 1
        elif a+b==2:
            i = 5
        elif a+b ==4:
            i = 9
    elif a > b: 
        if a + b == 1:
            i = 2
        elif a + b ==2:
            i = 3
        elif a + b == 3:
            i = 6
    elif a < b:
        if a + b == 1:
            i = 4
        elif a + b ==2:
            i = 7
        elif a + b == 3:
            i = 8
    return i 
a = list(map(int,input().split()))
row = {}
ver = {}
smallsedoku = {}
for i in range(0,9):
    for j in range(0,9):
        row[i][j] = [False]
        ver[i][j] = [False]
        smallsedoku[i][j] = [False]
row  = {[i/9-1][a[i]]:[True] for i in a}#0을 제외하고
ver = {[i%9-1][a[i]]:[True]for i in a}#0을 제외하고
smallsedoku = {[small(i)][a[i]:[True] for i in a]}#0을 제외하고
zerocount = []
for i in range(len(a)):
    if a[i] = 0:
        zerocount.append(i)
def sedouku(depth):
    for i in range(len(zerocount)):
            if  depth == len(zerocount):
                break
            for j in range(0,9):
                if  [False] == row[[zerocount[i]]/9-1][j] == ver[zerocount[i]%9-1][j] == smallsedoku[small[i]][j]:
                    continue
                    a[zerocount[i]] = row[[zerocount[i]]/9-1][j]
                    [True]  == row[zerocount[i]/9-1[i]][j] == ver[zerocount[i]%9-1][j] == smallsedoku[j]
                    sedouku(depth+1)
                    [False] == row[zerocount[i]/9-1[i]][j] == ver[zerocount[i]%9-1][j] == smallsedoku[j]
b = sedoku(0)
print(a)


