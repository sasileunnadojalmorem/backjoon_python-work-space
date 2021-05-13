#rgb거리:i번째 집을 각각의 색으로 칠할 때, 1~i번째 집을 모두 칠하는 최소 비용으로 부분문제를 정의해봅시다.
#색깔을 받을 2차원 배열 color_list선언
color_list = [[0 for _ in range(0,3)]for j in range(0,1002)]
n = int(input())
r = [0 for i in range(0,n)]
g = [0 for i in range(0,n)]
b = [0 for i in range(0,n)]
for i in range(0,n):
    r[i],g[i],b[i] = map(int,input().split())
#문제 조건 입출력
color_list[0][0] = r[0]
color_list[0][1] = g[0]
color_list[0][2] = b[0]
# 초기값 설정
for i in range(1,n):
    color_list[i][0] = min(color_list[i-1][1],color_list[i-1][2]) + r[i]
    color_list[i][1] = min(color_list[i-1][0],color_list[i-1][2]) + g[i]
    color_list[i][2] = min(color_list[i-1][0],color_list[i-1][1]) + b[i]
print(min(color_list[n-1]))