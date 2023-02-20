q=[]
q.append(1)
print(q)
q.pop(0)
print(q)

from collections import deque
que=deque([])
que.append(2)
print(que)
que.popleft()
print(que)

import queue
qq=queue.Queue()
qq.put(1)
print(qq.get())
print(qq.empty())