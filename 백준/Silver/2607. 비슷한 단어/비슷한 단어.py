# 2607. 비슷한 단어

import sys

enter = sys.stdin.readline

# 입력받는 단어의 갯수
N = int(enter().strip())

# 비교할 단어
target = list(enter().strip())

answer = 0
for _ in range(N - 1):
    # target deepcopy
    compare = target[:]

    # 비교할 단어 입력
    word = enter().strip()

    temp = 0
    for alphabet in word:
        # target에 포함된 알파벳이면 제거
        if alphabet in compare:
            compare.remove(alphabet)
        # 없다면 temp 1 증가
        else:
            temp += 1

    # 단어를 변화시킨게 1회 이하일 경우
    if temp <= 1 and len(compare) <= 1:
        answer += 1

print(answer)
