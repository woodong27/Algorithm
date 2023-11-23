# 20920. 영단어 암기는 괴로워

import sys

N, M = map(int, sys.stdin.readline().strip().split())

inputs = [sys.stdin.readline().rstrip() for _ in range(N)]
words = [word for word in inputs if len(word) >= M]

# 1. 자주 나오는 단어일수록 앞에 배치
# 2. 단어의 길이가 길 수록 앞에 배치
# 3. 알파벳 사전 순으로 앞 일수록 앞에 배치 == sort

# 1. 단어의 갯수 count
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

# 정렬 기준에 따라 sort
result = sorted(count.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for temp in result:
    print(temp[0])
