# 2212. 센서

import sys

enter = sys.stdin.readline

N = int(enter().strip())
K = int(enter().strip())
sensors = list(map(int, enter().strip().split()))
sensors.sort()

temp = []
for i in range(N - 1):
    # 각 센서들의 거리간의 차이를 저장
    temp.append(sensors[i+1] - sensors[i])

# 거리의 차이를 오름차순으로 정렬
temp.sort()

# 앞에서 n-k개를 더해주면 최소 합
answer = sum(temp[:N-K])

print(answer)
