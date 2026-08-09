qua = int(input())
n = int(input())
people = []


for _ in range(n):
    line = input().split()
    for i in range(4):
        if line[i]=='NJ':
            line[i]=0
    if (int(line[1]) >= qua) or (int(line[2]) >= qua) or (int(line[3]) >= qua):
        people.append(line[0])

if not people:
    print("Nobody qualifies!")
else:
    for i in people:
        print(i)