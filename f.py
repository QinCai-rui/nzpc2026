gaps = list(map(int, input().split()))
gaps.sort()
gaps.reverse()
n = int(input())

dogs = []
passed = []
for i in range(n):
    name, size = input().split()
    for i in range(len(gaps)):
        if int(size)<=min(gaps):
            passed.append(len(gaps))
            dogs.append(name)
            break
        if gaps[i]<int(size):
            if i==0:
                break
            passed.append(i)
            # print(i)
            dogs.append(name)
            break
if not passed:
    print('No dogs fit!')
    exit()
maximum=max(passed)
sorting=[]
for i in range(len(passed)):
    if passed[i]==maximum:
        sorting.append(dogs[i])
sorting.sort()
for i in sorting:
    print(i)