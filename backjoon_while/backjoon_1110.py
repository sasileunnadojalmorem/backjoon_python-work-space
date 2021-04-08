n = new_number = int(input())
count = 0
while True:
    ten = n//10 
    one = n%10
    res = ten + one
    count += 1
    n = int(str(n%10)+str(res%10))
    
    if (new_number==n):
        break
print(count)

    