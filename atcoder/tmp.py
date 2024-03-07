def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1  # 見つからない場合

a = [12, 43, 7, 15, 9]
sa = sorted(a)

ans = []

for i in range(len(a)):
    ans.append(binary_search(sa, a[i]))

print(ans)
