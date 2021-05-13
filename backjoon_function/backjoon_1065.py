def hansu(number):
    global count 
        
    if True: 
        q = list(str(number))
        char = int(q[0]) - int(q[1])
        if int(q[1]) - int(q[2]) == char:
            count = 1
        else :
            count = 0
    return count

a = int(input())
q =[]
for i in range(0,a):
    q.append(i)
c = 0

number = 99

if a>=100:
    for i in range(100,len(q)+1):
        
        hansu(i) 
        number =  count +number 
        
elif 100>a>0:
    number = len(q)

print(number)
    

















