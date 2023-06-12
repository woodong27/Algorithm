T=int(input())

for x in range(T):
    str1=input()
    str2=input()

    ans=0
    if str1 in str2:
        ans=1

    print(f'#{x+1} {ans}')