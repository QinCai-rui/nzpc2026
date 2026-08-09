from math import sqrt
num,fav=map(int, input().split())
# str='0'*num
k=['1']*fav+['0']*(num-fav)
# print(k)
for i in range(int(sqrt(num))):
    # print(i**2)
    # print(k[(i+1)**2])
    if k[(i+1)**2-1]=='1':
        k[(i+1)**2-1]='0'
    else:
        k[(i+1)**2-1]='1'
print(''.join(k))