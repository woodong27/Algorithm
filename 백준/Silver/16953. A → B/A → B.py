# 16953. A -> B

from collections import deque

A, B = map(int, input().split())

q = deque([(A, 1)])
answer = -1
while q:
    current, count = q.popleft()
    if current == B:
        answer = count
        break
    elif current < B:
        q.append((int(str(current) + "1"), count + 1))
        q.append((current * 2, count + 1))

print(answer)
