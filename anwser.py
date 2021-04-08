#문제: N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
#입력:첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
#출력: 첫째 줄에 주어진 정수 n개의 최솟값과 최대값을 공백으로 구별해 출력한다.


a = [5,0,3,2,4]


result = a[0]
for i in range(len(a)): # 비 권장 방법
    if result < a[i]:
        result = a[i]
print(result)

result = a[0]
for i in range(len(a)):
    if result > a[i]:
        result = a[i]
print(result)


result = a[0]
for idx, item in enumerate(a):
    if result > a[i]:
        result = a[i]
print(result)


# 리스트 == 배열

import numpy as np

print(np.log(2))

a = np.array([1,2,3,4,5,7,6])

print(a)


n = int(input())
number = map(int,input().split())
num = number.array




# print(num[0] + num [n-1])