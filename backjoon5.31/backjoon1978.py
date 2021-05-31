_ = int(input())
n = list(map(int,input().split()))
cnt = 0
def sum(n):
    if n == 1:
        return False
    for i in range(2,int((n**0.5))+1):
        if n%i == 0:
            return False
    return True
for i in range(len(n)):
    if sum(n[i]) == True:
        cnt +=1
print(cnt)