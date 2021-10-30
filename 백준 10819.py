from itertools import permutations
N = int(input())
A = sorted(map(int, input().split()))
per_A = list(permutations(A, N))  # A 원소 순서의 모든 경우를 구함
res = 0
for i in per_A:
    temp = 0
    for j in range(len(i)-1):
        temp += abs(i[j+1] - i[j])
    res = max(res, temp)
print(res)
