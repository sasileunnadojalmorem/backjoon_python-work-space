def d(n):
    a = 0
    b = list(str(n))
    for i in b:
        a += int(i)
    a = a + n
    return a
a=[]
for i in range(1,10001):
    k = d(i)
    a.append(k)
for b in range(1, 10001):
    if b in a:
        pass
    else:
        print(b)
#실패!!!!!!!!