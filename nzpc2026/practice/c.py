line = input().split()
balance = int(line[0])

def func(action, num):
    global balance
    if action == "W":
        if int(num)-1 > balance:
            print("Not Allowed")
        else:
            balance -= int(num)
            print(balance)
    if action == "D":
        balance += int(num)
        print(balance)
line = input().split()

while line[0] != "END":
    q, w = line
    func(q,w)
    line = input().split()

