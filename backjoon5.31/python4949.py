from collections import deque
n = str(input())

def balence(s):
    stack = deque()
    for i in range(len(s)):
        if s[i] == '[':
            stack.append('[')
        elif s[i] == '(':
            stack.append('(')
        elif s[i] == ']':
            if len(stack) >=1:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False
        elif s[i] == ')':
            if len(stack) >=1:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack) != 0:
        return False
    return True
while n != '.':
    a = balence(n)
    if a == True:
        print('yes')
    else:
        print('no')
    n = str(input())
