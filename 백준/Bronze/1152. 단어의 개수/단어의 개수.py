# 1152. 단어의 개수

import sys

# 입력받은 문장을 공백으로 나눠줌
words = list(sys.stdin.readline().strip().split(' '))

# 빈 문장이 올 경우 삭제
if '' in words:
    words.remove('')

# 단어의 갯수를 세어줌
answer = len(words)
print(answer)
