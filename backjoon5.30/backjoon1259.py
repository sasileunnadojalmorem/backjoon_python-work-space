s = 1
while s != '0':
    s = str(input())
    a = []
    if s == '0':
        break
    for i in range(len(s)):
        a.append(s[i])
    b = list(a.__reversed__())
    if a == b:
        print('yes')
    else:
        print('no')