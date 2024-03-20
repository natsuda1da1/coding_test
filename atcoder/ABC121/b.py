N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = list(list(map(int, input().split())) for _ in range(N))

ans = 0

for i in range(N):
    score = 0
    for j in range(M):
        score += A[i][j]*B[j]
    if score + C > 0:
        ans += 1

print(ans)
        


