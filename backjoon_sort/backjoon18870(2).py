n = int(input())
a=list(map(int,input().split()))``
b=list(sorted(set(a)))
b = {b[i]:i for i in range(len(b))}
a = [b[a[i]] for i in range(len(a))]
print(*a)
