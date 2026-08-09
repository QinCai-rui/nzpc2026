team1=[input().split(),input().split()]
team2=[input().split(),input().split()]
handicap1=int(team1[0][1])+int(team1[1][1])
handicap2=int(team2[0][1])+int(team2[1][1])
diff=abs(handicap1-handicap2)
diff /= 2
if int(diff)==diff:
    diff=int(diff)
if handicap1>handicap2:
    if diff == 1:
        print(f'1 bisque is awarded to {team2[0][0]} and {team2[1][0]}.')
    else:print(f'{diff} bisques are awarded to {team1[0][0]} and {team1[1][0]}.')
elif handicap1<handicap2:
    if diff == 1:
        print(f'1 bisque is awarded to {team2[0][0]} and {team2[1][0]}.')
    else:print(f'{diff} bisques are awarded to {team2[0][0]} and {team2[1][0]}.')
else:
    print('No bisques are awarded.')