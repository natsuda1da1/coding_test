N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))

m = set()
for a in A:
    for b in B:
        for c in C:
            m.add(a+b+c)

Q = int(input())
X = list(map(int, input().split()))

for x in X:
    if x in m:
        print('Yes')
    else:
        print('No')
