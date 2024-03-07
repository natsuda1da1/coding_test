N = int(input())

H, S = [], []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

l, r = 0, 1<<60

while (r - l > 1):
    mid = (r + l) / 2
    flag = True
    t = [0]*N

    for i in range(N):
        if mid < H[i]:
            flag = False
        else:
            t[i] = (mid - H[i]) / S[i]
    t.sort()

    for j in range(N):
        if t[j] < j:
            flag = False

    if flag:
        r = mid
    else:
        l = mid

print(int(r))



