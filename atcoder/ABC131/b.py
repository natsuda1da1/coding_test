if __name__ == '__main__':
    N, L = map(int, input().split())
    ans = 0
    min_abs = float('inf')

    for i in range(1, N+1):
        ans += L+i-1
        if abs(L+i-1) < min_abs:
            min_abs = abs(L+i-1)
            real_num = L+i-1    
    print(ans-real_num)
