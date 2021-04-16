def small(i):
    c = (i/9-1) / 3
    b = (i%9-1) / 3
    if c == b:
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
a =[]
for i in range(0,9):
    b = list(map(int,input().split()))  
    for j in range(len(b)):
        a.append(b[j])
row = []
ver = []
smallsedoku = []
q = []
for j in range(0,9):
    for i in range(0,9):
        q.append(i+1)
    row.extend(q)
    ver.extend(q)
    smallsedoku.extend(q)
for i in range(len(a)):
    if a[i] != 0 :
        row[i//9-1][a[i]-1] = 10
        ver[i%9-1][a[i]-1] = 10
        smallsedoku[small(i)][a[i]] = 10 
zerocount = []
for i in range(len(a)):
    if a[i] == 0:
        zerocount.append(i)
def sedouku(depth):
    for i in range(len(zerocount)):
            if  depth == len(zerocount):
                break
            for j in range(0,9):
                if  j+1 == row[[zerocount[i]]//9-1][j] == ver[zerocount[i]%9-1][j] == smallsedoku[small[i]][j]:
                    continue
                    a[zerocount[i]] = j+1
                    row[zerocount[i]//9-1[i]][j] = 10
                    ver[zerocount[i]%9-1][j] = 10
                    smallsedoku[small[i]][j] = 10
                    sedouku(depth+1)
                    row[zerocount[i]//9-1[i]][j] = j+1
                    ver[zerocount[i]%9-1][j] = j+1
                    smallsedoku[small[i]][j] = j+1
b = sedoku(0)
print(a)




