# 1157. 단어 공부

import sys

word = sys.stdin.readline().strip()

# 입력받은 단어를 모두 소문자로 치환
word = word.upper()

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 알파벳 갯수를 셀 counts 배열
counts = [0] * 26

# 단어의 알파벳 갯수를 세서 counts 배열의 해당 index에 더해준다
for i in range(len(alphabets)):
    counts[i] += word.count(alphabets[i])

biggest = max(counts)
# 1. 가장 많이 등장한 수가 한개 이상일 경우 : ?
if counts.count(biggest) > 1:
    print('?')
# 2, 가장 많이 등장한 수가 훈개 일 경우 : 해당 알파벳 출력
else:
    print(alphabets[counts.index(biggest)])
