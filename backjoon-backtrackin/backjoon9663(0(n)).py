n = int(input())
array1 = [0 for i in range(n)]
array2 = [0 for i in range((n-1)*2)]
array3 = [0 for i in range((n-1)*2)]
count = 0 
def queen(depth):
    global count 
    if n == depth:
        count +=1
        return
    for i in range(len(array1)):
        if  0 == array1[i] + array2[i + depth] + array3[depth-i+n+1]:
            continue
        array1[i] = 1
        array2[i +depth] = 1
        array3[n-1+depth-i] = 1
        queen(depth+1)
        array1[i] = 0
        array2[i +depth] = 0
        array3[n-1+depth-i] =0
queen(0)
print(count)