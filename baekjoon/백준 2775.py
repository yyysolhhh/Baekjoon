T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1, n+1)]
    for i in range(0, k):
        for j in range(1, n):
            floor[j] += floor[j-1]
    print(floor[-1])
