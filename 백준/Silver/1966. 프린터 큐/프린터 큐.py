# BOJ 1966 S3 프린터 큐

from collections import deque

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    papers = list(map(int, input().split()))
    papers = deque([[i, papers[i]] for i in range(n)])

    current_length = len(papers)
    answer = 0
    while papers:
        number, current = papers.popleft()
        for idx, paper in papers:
            if paper > current:
                papers.append([number, current])
                break

        if len(papers) != current_length:
            current_length = len(papers)
            answer += 1
            if number == m:
                break

    print(answer)
