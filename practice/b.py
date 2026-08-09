targ = int(input())
n = int(input())
people = []

for _ in range(n):
    _input = input().split()
    person = _input[0]
    guess = _input[1]
    people.append([person, guess])

closest=1000000000000
for i in people:
    var=int(i[1])
    var=abs(var-targ)
    if var<closest:
        closest=abs(int(i[1])-targ)
for i in people:
    if abs(int(i[1])-targ)==closest:
        print(i[0])
        break
