# 문제 코드
# def fibonacci(n):
#     if n == 0:
#         print(0)
#         return 0
#     elif n == 1:
#         print(1)
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


T = int(input())
dp = [[0] * 2 for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1
for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])
