if __name__ == '__main__':
    a = []
    b = []
    a.sort()
    b.sort()
    
    i, j = 0, 0
    ans = 0
    while i < len(a) or j < len(b):
        if a[i] < b[j]:
            i += 1
            j += 1
            ans += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1

    print(ans)

