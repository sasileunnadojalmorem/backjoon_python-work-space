import sys
input = sys.stdin.readline
def cul(i,nums,add,m,mul,div):
    global minv,maxv
    if i == n:
        maxv = max(nums,maxv)
        minv = min(nums,minv)
        return
    else:
        if add:
            cul(i+1, nums+num_list[i], q[0]-1,q[1],q[2],q[3])
        if m:
            cul(i+1, nums-num_list[i], q[0],q[1]-1,q[2],q[3])
        if mul:
            cul(i+1, nums*num_list[i], q[0],q[1],q[2]-1,q[3])
        if div:
            cul(i+1, int(nums/num_list[i]),q[0],q[1],q[2],q[3]-1)
n = int(input())
num_list = list(map(int,input().split()))
q = list(map(int,input().split()))
minv, maxv = 1e9, -1e9
cul(1,num_list[0],q[0],q[1],q[2],q[3])
print(maxv)
print(minv)