N = int(input())
P = list(map(int, input().split()))

dp = [[False]*(sum(P)+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = True
    dp[i][P[i-1]] = True

    for j in range(sum(P)+1):
        if dp[i-1][j] == True:
            dp[i][j] = True
            dp[i][j+P[i-1]] = True

ans = 0
for flag in dp[-1]:
    if flag == True:
        ans += 1

print(ans)





