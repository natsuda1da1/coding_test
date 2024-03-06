s = input()
t = input()

dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]

words = ''
for i in range(len(t)):
    for j in range(len(s)):
        if t[i] == s[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(words)

#https://maku.blog/p/a3jyhwd/