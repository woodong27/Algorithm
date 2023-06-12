T=int(input())

code={'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,
      '0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

for tc in range(T):
    N,M=map(int,input().split())
    password=[list(input())for _ in range(N)]

    temp=[]
    for i in range(N):
        for j in range(M-1,-1,-1):
            if password[i][j]=='1':
                temp=password[i][j-55:j+1]
                break

    trans=[]
    for i in range(0,56,7):
        trans.append(code[''.join(temp[i:i+7])])

    temp1=0
    temp2=0
    for i in range(8):
        if i%2:
            temp1+=trans[i]
        else:
            temp2+=trans[i]

    ans=0
    if not (temp1+temp2*3)%10:
        ans=sum(trans)

    print(f'#{tc+1} {ans}')