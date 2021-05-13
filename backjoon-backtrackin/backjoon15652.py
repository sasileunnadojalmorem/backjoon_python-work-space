N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

def solve(depth,idx, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))
                                                                                                                        
        return
    for i in range(idx,N):  
        if not visited[i]:  
            out.append(i+1) 
            
            solve(depth+1,i, N, M)
            out.pop()
           
            
            
solve(0, 0, N, M)