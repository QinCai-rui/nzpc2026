bank=[1,2,3,4,5,5,6,6,6]
mults=[]
integer=int(input())
num=1
while num<=integer:
    num=10*num+1
num=(num-1)//10
def degrade(n):
    return (n-1)//10
while True:
    for i in range(1,10):
        if i*num>integer:
            mults.append(i-1)
            num=degrade(num)
            break
    if num==0:
        break
print(mults)