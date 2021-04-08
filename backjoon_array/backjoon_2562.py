a = 9
b = []
for i in range(a):
    c = int(input())
    b.append(c)
print(max(b))
e = int(b.index(max(b))) + 1
print(e)