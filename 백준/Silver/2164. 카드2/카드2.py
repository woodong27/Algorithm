# 2164. 카드2

import sys
from collections import deque

N = int(sys.stdin.readline().strip())

# 1~N을 원소로 가진 q 선언
q = deque([i+1 for i in range(N)])

# q의 길이가 1이 될 때 까지 반복
while len(q) > 1:
    # 1. 가장 위의 카드를 빼주고
    q.popleft()
    # 2. 다음 카드를 가장 아래로 이동 시킴
    q.append(q.popleft())

# 한 장 남았을 때 결과 출력
print(q[0])
