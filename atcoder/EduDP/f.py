s = input()
t = input()

dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]

for i in range(len(t)):
    for j in range(len(s)):
        if t[i] == s[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

i, j , tmp = 0, 0, 0

ans = ''

while i < len(t) and j < len(s):
    if dp[i+1][j+1] > tmp:
        ans += s[i]
        i += 1
        j += 1
    elif dp[i][j+1] > tmp:
        ans += s[i]
        

#https://maku.blog/p/a3jyhwd/