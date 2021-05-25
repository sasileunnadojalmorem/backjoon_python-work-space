#45분 일찍 설정하기
#입력: 첫쨰 줄에 h와 m을  설정하자
#출력: 상근이가 창영이의 방법을 사용할떄 :알람 시간을 출력하자 ex)10 10 > 9 25
h,m = map(int,input().split())
if m>44:
    m=m-45
    print(h,m)
elif m<45 and h>0:
    print(h-1,m+15)
else:
    
    print(23,m+15)
       

    