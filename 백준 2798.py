import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                result = max(sum, result)
print(result)
