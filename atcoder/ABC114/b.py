S = input()

ans = float('inf')

for i in range(len(S)-2):
    if abs(753 - int(S[i:i+3])) < ans:
        ans = abs(753 - int(S[i:i+3]))

print(ans)
