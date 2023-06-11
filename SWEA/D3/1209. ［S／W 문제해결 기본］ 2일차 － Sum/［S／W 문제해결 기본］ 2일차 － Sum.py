for x in range(10): #전체 루프 10번 반복
    T=int(input()) #테스트 케이스 번호를 받을 변수
    l=[[0 for x in range(100)]for x in range(100)] #배열을 받을 리스트
    for k in range(100):
        l[k]=list(map(int,input().split()))

    #각 행의 합
    row=[0 for x in range(100)] #배열의 행의 합을 입력받을 리스트(0으로 초기화)
    for i in range(100):
        for j in range(100):
            row[i]=row[i]+l[i][j]

    #각 열의 합
    col=[0 for x in range(100)] #열의 합을 입력받을 리스트(0으로 초기화)
    for i in range(100):
        for j in range(100):
            col[i]=col[i]+l[j][i]

    #대각선의 합
    diag=[0 for x in range(2)] #대각선의 합을 입력받을 리스트(0으로 초기화)
    for i in range(2):
        for j in range(100):
            diag[i]=diag[i]+l[j][j]

    row.sort()
    col.sort()
    diag.sort() #각 list를 모두 정렬시켜서 가장 큰 값이 마지막 index로 이동

    max = 0  # 행/열/대각선의 합중 가장 큰 값을 반환받을 변수

    if row[-1]>=col[-1] and row[-1]>=diag[-1]:
        max=row[-1]
    elif row[-1]>=col[-1] and row[-1]<=diag[-1]:
        max=diag[-1]
    elif row[-1]<=col[-1] and row[-1]>=diag[-1]:
        max=col[-1]
    elif row[-1]<=col[-1] and row[-1]<=diag[-1]:
        if col[-1]>=diag[-1]:
            max=col[-1]
        elif col[-1]<=diag[-1]:
            max=diag[-1]

    print(f'#{x+1} {max}')
