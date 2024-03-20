N, M = map(int, input().split())
drinks = list(list(map(int, input().split())) for _ in range(N))
drinks.sort(key=lambda x: x[0])

value = 0
for i in range(N):
    if drinks[i][1] < M:
        value += drinks[i][0]*drinks[i][1]
        M -= drinks[i][1]
    else:
        value += drinks[i][0]*M
        print(value)
        break

