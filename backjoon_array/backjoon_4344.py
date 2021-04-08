#문제: 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
c = int(input())
number = 0 
avrage = 0
count = 0
last = 0 
for i in range(0,c):
    a = list(map(int,input().split()))
    for j in range(1,len(a)):
        number += a[j]
    avrage = number/(len(a)-1)
    for q in range(1,len(a)):
        if a[q]>avrage :
            count +=1 
    last = (str("%.3f" %round((count/(len(a)-1))*100, 3))+"%")
    print(last)
    count = 0
    number = 0
    avrage = 0
    last =0

    
        