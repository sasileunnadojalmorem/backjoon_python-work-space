#문제 z: 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다
n,a,b = map(int,input().split())
number_list = [[0 for i in range(2**n)]for j in range(2**n)] #2 차원 배열 선언
cnt = 0
def z(n,q,i): #n은 사각형의 크기,q는 사각형의 위치 ,cnt는 가로지르는 횟수
    global cnt
    if n = 1:
        number_list[i] = cnt
        number_list[i+1] = cnt
        cnt += 1
        return
    z(n-1,1,0,0,i+q)#1번째 사각형
    z(n-1,2,i+q)#2번째 사각형
    z(n-1,3,i+q)#3번째 사각형
    z(n-1,4,i+q)#4번쨰 사각형
n(2,0,0)
#@만약 사각형의 크기가 8*8이면 얼마나 쪼갤까 8/2 3번 쪼갬 사각형의 개수 8*8이 어떻게 표시할까? 사각형의 위치
