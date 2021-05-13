N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

def solve(depth, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    
    for i in range(len(visited)):  
        if not visited[i]: 
            visited[i] = True  
            out.append(i+1)
            solve(depth+1, N, M)  
            visited[i] = False 
            out.pop()  

solve(0, N, M)