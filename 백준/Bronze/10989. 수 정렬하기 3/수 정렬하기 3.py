import sys

N=int(sys.stdin.readline().rstrip())
counts=[0]*10001
for _ in range(N):
    counts[int(sys.stdin.readline().rstrip())]+=1

for i in range(1,10001):
    if counts[i]:
        for j in range(counts[i]):
            sys.stdout.write(str(i)+'\n')