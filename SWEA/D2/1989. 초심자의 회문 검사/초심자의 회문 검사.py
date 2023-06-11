T=int(input())

for x in range(T):
    word=input()

    ans=0
    if word==word[::-1]:
        ans=1

    print(f'#{x+1} {ans}')