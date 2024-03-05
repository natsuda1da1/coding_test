def recursive(A, cnt):
    tmp = []
    Flag = True
    for num in A:
        if num % 2 != 0:
            Flag = False
            break
        else:
            tmp.append(int(num//2))
    if Flag:
        return recursive(tmp, cnt+1)
    else:
        return cnt    

N = int(input())
A = list(map(int, input().split()))

cnt = 0

print(recursive(A, cnt))

