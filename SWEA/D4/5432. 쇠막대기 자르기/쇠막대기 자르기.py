T=int(input())

for x in range(T):
    line=input()
    line=line.replace('()','L')

    ans=0
    stick=0
    for i in line:
        if i=='L':
            ans+=stick
        elif i=='(':
            stick+=1
        else:
            stick-=1
            ans+=1

    print(f'#{x+1} {ans}')