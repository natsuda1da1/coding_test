## https://atcoder.jp/contests/abc077/tasks/arc084_a

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    B.sort()
    C.sort()

    answer = 0
    for b in B:
        # bよりも真に小さいAの個数
        if b <= A[0]:
            continue

        low = 0
        high = N - 1
        while high - low > 1:
            mid = (high + low) // 2
            if A[mid] < b:
                low = mid
            else:
                high = mid
        if A[high] < b:
            a_v = high
        else:
            a_v = low
        
        a_num = a_v + 1

        # bよりも真に大きいCの個数
        if b >= C[-1]:
            continue
        
        low = 0
        high = N - 1
        while high - low > 1:
            mid = (high + low) // 2
            if C[mid] > b:
                high = mid
            else:
                low = mid
        if C[low] > b:
            c_v = low
        else:
            c_v = high
        c_num = N - c_v

        ans = a_num * c_num
        answer += ans
    print(answer)





   
if __name__ == "__main__":
    main()
