n = int(input())
a,b = map(int,input().split())
maxsize = int(input())
c = [a,b]
#길이가 2이고 무게가  maxsize를 못넘는 모든 함수를 구한다
for i in range(0,n):