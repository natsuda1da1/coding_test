def recursive(num, ans):
    if int(num) > N:
        return ans
    if '7' in num and '5' in num and '3' in num:
        ans += 1
    recursive(num+'7', ans)
    recursive(num+'5', ans)
    recursive(num+'3', ans)

N = int(input())
ans = 0

ans += recursive('3', 0)
ans += recursive('5', 0)
ans += recursive('7', 0)

print(ans)


