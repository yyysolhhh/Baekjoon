import sys
input = sys.stdin.readline
n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

# 1
dp = []
dp.append(stairs[0])
dp.append(stairs[0] + stairs[1])
dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
for i in range(3, n):
    dp.append(max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i]))
print(dp[n-1])

# 2
dp = [0 for _ in range(n)]
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
for i in range(3, n):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
print(dp[n-1])
