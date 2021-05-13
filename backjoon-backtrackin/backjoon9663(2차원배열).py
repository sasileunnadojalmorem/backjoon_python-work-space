n = int(input())
a = []
for i in range(0,n):
    a.append([])
    for j in range(0,n):
        a[i].append([False])
# 2차원 배열 완성 n과 m과 마찬가지로 visited속성을 가진다
# 함수 선언
def queen(depth,a,q):
    if len(a)+1 = depth:
        count +=1
        return
    for i in range(q,len(a)):
            for j in range(len(a)):
                if not a[i][j]:
                    #퀸의 경우의 수만큼 체스판들을 true로 만들어준다
                    queen(depth+1,a,q)
                    #전에 놓았던 퀸의 경우의 수만큼 체스판들을 false로 만들어준다.
                else:
                    return
            
                
    return count
a = queen(0,a,0)
print(a)
            



