x = int(input())
q = 1
cnt = 0
while q<x:
    q = 3**cnt
    cnt = cnt + 1
ba = [[['*'for q in range(0,1)] for i in range(0,1)] for x in range(0,1)]
for i in range(0,8):
    ba.append(0)
for n in range(1,cnt):
    sa =[[' 'for i in range(0,3**n)]for j in range(0,3**n)]
    starpoint = list(ba[n-1])
    for j in range(0,len(starpoint)*3):
        for i in range(0,3):
            if j>= 3**(n-1) and j<3**(n-1)*2 and i == 1 :
                opo = 0 
            else:
                sa[j][i*(3**(n-1)):(i+1)*(3**(n-1))] =  starpoint[(j)%(3**(n-1))][0:3**(n-1)]
    ba[n] = sa
for row in ba[cnt-1]:
    print(''.join(row))