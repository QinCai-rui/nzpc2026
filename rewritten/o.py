t=int(input())
for i in range(t):
    n=int(input())
    elements=list(map(int,input().split()))
    q=int(input())
    for j in range(q):
        comp=[]
        l,r=map(int,input().split())
        for k in range(l-1,r):
            if elements[k] in comp:
                remove=comp.index(elements[k])
                comp=comp[:remove]
            else:
                comp.append(elements[k])
        print(len(comp))
