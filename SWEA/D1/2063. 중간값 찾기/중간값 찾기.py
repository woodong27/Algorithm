n=int(input())
score=[int(x) for x in input().split()]
score.sort()
print(score[n//2])