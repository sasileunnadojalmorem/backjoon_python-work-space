d = [0 for i in range(22)]
d[0] = 0
d[1] = 1
for i in range(2,22):
    d[i] = d[i-2] + d[i-1]
n = int(input())
print(d[n])