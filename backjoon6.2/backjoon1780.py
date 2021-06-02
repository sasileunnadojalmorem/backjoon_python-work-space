import sys
from typing import Tuple
input = sys.stdin.readline
n = int(input())
lis = [list(map(int,input().split())) for i in range(n)]
dic = {-1:0,0:0,1:0}
def devide(x,y,q):
    if q == 1:
        dic[lis[x][y]] +=1
        print(x,y)
        return
    def same(x,y,q): 
        a = lis[y][x]
        for i in range(y,y+q):
            for j in range(x,x+q):
                if a != lis[i][j]:
                    return False
        dic[a] = dic[a] + 1     
        return True
    answer = same(x,y,q)
    if answer == True:
        return
    else:
        for j in (y,y + q//3,y + 2*(q//3)):
            for i in (x, x + q//3,x + 2*(q//3)):
                devide(j,i,q//3)
    return
    
devide(0,0,n)   
print(dic)

