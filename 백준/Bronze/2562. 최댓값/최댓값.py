# 2562. 최댓값

maxNum = 0
maxIndex = 0

for i in range(1, 10):
    number = int(input())
    if number > maxNum:
        maxNum = number
        maxIndex = i

print(maxNum)
print(maxIndex)