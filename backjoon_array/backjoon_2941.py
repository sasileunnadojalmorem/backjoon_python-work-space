a = str(input())
b = list(a)
count = 0
while len(b)> 0:
    c = str(b[len(b)-2:len(b)])
    if (c =='dz'):
        b.pop()
    elif c =='c=' or c =='c-' or c =='d-' or c =='lj'or c =='nj'or c =='s=' or c =='z=':
        b.pop()
    else:
        b.pop()
    count +=1
    
print(count)
        
    
