N = int(input())

dp = [[0]*(N+1) for _ in range(3)]

for i in range(N):
    a, b, c = map(int, input().split())

    dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + a
    dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + b
    dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + c

print(max(dp[0][N-1], dp[1][N-1], dp[2][N-1]))

