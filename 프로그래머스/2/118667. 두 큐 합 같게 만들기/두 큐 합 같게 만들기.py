from collections import deque

def solution(queue1, queue2):  
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1, sum2 = sum(queue1), sum(queue2)
    answer = 0
    end = len(queue1) * 3
    while True:
        if sum1 == sum2:
            return answer
        
        if sum1 > sum2:
            q2.append(q1.popleft())
            sum1 -= q2[-1]
            sum2 += q2[-1]
        else:
            q1.append(q2.popleft())
            sum1 += q1[-1]
            sum2 -= q1[-1]
        answer += 1
            
        if answer >= end:
            return -1
        