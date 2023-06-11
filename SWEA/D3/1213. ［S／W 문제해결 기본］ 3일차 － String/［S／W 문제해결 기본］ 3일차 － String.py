for i in range(10):
    tc=int(input())

    target=input()
    sentence=input()

    count = 0
    while target in sentence:
        sentence=sentence.replace(target,'',1)
        count+=1

    print(f'#{tc} {count}')