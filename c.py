n,r=map(int,input().split())
line=list(map(int,input().split()))
minimum = 100000000
i = 0
while i+r-1 < len(line):
    _sum = sum(line[i:i+r])
    if _sum < minimum:
        minimum = _sum
    i += 1
print(minimum)
