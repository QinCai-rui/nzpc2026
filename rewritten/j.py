l0=['1111110','0111110','1011110','1101110','1110110','1111010','1111100']
l1=['0110000','0010000','0100000']
l2=['1101101','0101101','1001101','1100101','1101001','1101101']
l3=['1111001','0111001','1011001','1101001','1110001','1111000']
l4=['0110011','0010011','0100011','0110001','0110010']
l5=['1011011','0011011','1001011','1010011','1011001','1011010']
l6=['1011111','0011111','1001111','1010111','1011011','1011101','1011110']
l7=['1110000','0110000','1010000','1100000']
l8=['1111111','0111111','1011111','1101111','1110111','1111011','1111101','1111110']
l9=['1111011','0111011','1011011','1101011','1110011','1111001','1111010']
maps=[l0,l1,l2,l3,l4,l5,l6,l7,l8,l9]

n,q=map(int,input().split())
digits=[]
for i in range(n):
    digits.append(input().strip())

inputs=[]
for i in range(n):
    p=[]
    for j in range(10):
        if digits[i] in maps[j]:
            p.append(j)
    inputs.append(sorted(set(p),reverse=True))

if [] in inputs:
    print('ERROR')
    exit()

suffix_products=[1]*(n+1)
for i in range(n-1,-1,-1):
    suffix_products[i]=suffix_products[i+1]*len(inputs[i])
    if suffix_products[i]>10**6:
        suffix_products[i]=10**6+1

def length(digited):
    c=1
    for i in digited:
        c*=len(i)
        if c>10**6:
            c=10**6+1
            break
    return c

def find(digited,k):
    res=[]
    n=len(digited)
    for i in range(n):
        for j in digited[i]:
            c=suffix_products[i+1]
            if k<=c:
                res.append(str(j))
                break
            else:
                k-=c
    return ''.join(res)

for e in range(q):
    k=int(input().strip())
    if k>length(inputs):
        print('NONEXISTENT')
    else:
        print(find(inputs,k))
