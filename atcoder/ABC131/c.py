import math


if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    
    div_c = B//C - (A-1)//C
    div_d = B//D - (A-1)//D
    lcm = math.lcm(C, D) #最小公倍数
    div_cd = B//lcm - (A-1)//lcm

    ans = B-(A-1)-(div_c+div_d-div_cd)

    print(ans)




