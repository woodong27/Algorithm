# 23971. ZOAC 4

import sys
import math

H, W, N, M = map(int, sys.stdin.readline().strip().split())

answer = math.ceil(H / (1 + N)) * math.ceil(W / (1 + M))

print(answer)