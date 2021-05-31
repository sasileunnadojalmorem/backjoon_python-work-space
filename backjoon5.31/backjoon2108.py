from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
lis = []
for i in range(n):
    s= int(input())
    lis.append(s)
lis.sort()
k=Counter(lis).most_common()
print(round(sum(lis)/n))
print(lis[n//2])
if len(lis) > 1: 
    if k[0][1] == k[1][1]:print(k[1][0]) 
    else : print(k[0][0]) 
else : print(lis[0]) 
print(lis[-1]-lis[0])
