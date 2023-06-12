T=int(input())

def babygin(player):
    if len(player)>=3:
        for card in player:
            if player.count(card)==3:
                return 1

        cnt_run=0
        player.sort()
        player=list(set(player))
        for i in range(len(player)-1):
            if player[i+1]==player[i]+1:
                cnt_run+=1
                if cnt_run>=2:
                    return 1
            else:
                cnt_run=0

    return 0

for tc in range(T):
    cards=list(map(int,input().split()))

    win=0
    player1,player2=[],[]
    for i in range(len(cards)):
        if i%2:
            player2.append(cards[i])
        else:
            player1.append(cards[i])

        if babygin(player1)==1:
            win=1
            break
        elif babygin(player2)==1:
            win=2
            break

    print(f'#{tc+1} {win}')