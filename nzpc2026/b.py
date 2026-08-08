_max=0
n=int(input())
s1=list(map(int, input().split()))
s2=list(map(int, input().split()))
streak=0
for i in range(n):
    if s1[i]<s2[i]:

        streak+=1
        if _max<streak:
            _max=streak
    else:

        streak=0
print(_max)
'''

n = int(input())
claire = input().split()
mai = input().split()

max_streak = 0
streak = 0
for i in range(n):
    if claire[i] < mai[i]:
        streak += 1
        if streak > max_streak:
            max_streak = streak
    else:
        streak = 0

print(max_streak)

'''