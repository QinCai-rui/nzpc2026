_input = input().split()
symbol = _input[0]
h = int(_input[1])
t = int(_input[2])
gap = h - t - 1

buffer = [[symbol]*h]*t+[[]]*gap+[[symbol]*h]*t
# for i in range(t):
for i in range(gap):
    buffer[i+t]=[' ']*(i+1)+[symbol]*(t)+[' ']*(h-t-i-1)
# for row in range(h):
#     for column in range(h+t+gap):

for j in range(h):
    buffer2=''
    for i in buffer:
        buffer2+=i[j]
    print(buffer2)