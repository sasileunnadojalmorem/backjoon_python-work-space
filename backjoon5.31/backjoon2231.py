import sys
input = sys.stdin.readline
def sumsum(q):
    if q<=54:
        for i in range(1,q):
            a = str(i)
            sum = i
            for j in range(len(a)):
                sum += int(a[j])
            if q == sum:
                return i 
        return 0
    elif q>54:
        for i in range(q-54,q):
            a = str(i)
            sum = i
            for j in range(len(a)):
                sum += int(a[j])
            if q == sum:
                return i 
        return 0

n = int(input())
answer = sumsum(n)
print(answer)
