def small(i):
    c = (i//9)// 3
    b = (i%9)// 3
    if c == b:
        if c+b == 0:
            ans = 0
            return ans
        elif c+b==2:
            ans = 4
            return ans
        elif c+b ==4:
            ans = 8
            return ans
    elif c > b: 
        if c + b == 1:
            ans = 1
            return ans
        elif c + b ==2:
            ans = 2
            return ans
        elif c + b == 3:
            ans = 5
            return ans
    elif c < b:
        if c + b == 1:
            ans = 3
            return ans
        elif c + b ==2:
            ans = 6
            return ans
        elif c + b == 3:
            ans = 7
            return ans
a = small(81)
print(a)
a =[]
row = []
ver = []
smallsedoku = []
q = []
for j in range(0,9):
    q.append(j+1)
for j in range(0,9):
    row.extend([q])
    ver.extend([q])
    smallsedoku.extend([q])
for i in range(0,9):
    b = list(map(int,input().split()))  
    for j in range(len(b)):
        a.append(b[j])

for i in range(0,len(a)):
    if a[i] != 0 :
        row[(i+1)//9][a[i]-1] = 10
        ver[(1+i)%9-1][a[i]-1] = 10
        smallsedoku[small(i+1)][a[i]-1] = 10 
zerocount = []
for i in range(len(a)):
    if a[i] == 0:
        zerocount.append(i)
def sedouku(depth):
    for i in range(len(zerocount)):
            if  depth == len(zerocount):
                break
            for j in range(0,9):
                if  j+1 == row[(1+[zerocount[i]])//9][j] and j+1 == ver[(1+zerocount[i])%9-1][j] and j+1 == smallsedoku[small(i+1)][j]:
                    continue
                    a[zerocount[i]] = j+1
                    row[(1+zerocount[i])//9][j] = 10
                    ver[(1+zerocount[i])%9-1][j] = 10
                    smallsedoku[small(i+1)][j] = 10
                    sedouku(depth+1)
                    row[(1+zerocount[i])//9][j] = j+1
                    ver[(1+zerocount[i])%9-1][j] = j+1
                    smallsedoku[small(i+1)][j] = j+1
b = sedoku(0)
print(a)





