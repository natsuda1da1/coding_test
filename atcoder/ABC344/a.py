S = input()
S = S.split('|')
ans = ''
for i in range(len(S)):
    if i % 2 == 0:
        ans += S[i]
print(ans)
