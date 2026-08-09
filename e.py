month = input()
loc = input()
n = int(input())

stores = []
scores=[]
for i in range(n):
    store,scoreABC=input().split(',')
    score=0
    for i in scoreABC.split():
        if i=='A':
            score+=5
        elif i=='B':
            score+=2
    if store not in stores:
        stores.append(store)
        scores.append(score)
    else:
        scores[stores.index(store)]+=score
maximum=max(scores)
print(f'{stores[scores.index(maximum)]} was Store of the Month for {loc} in {month}.')