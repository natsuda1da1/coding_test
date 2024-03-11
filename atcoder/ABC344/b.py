A = []
while True:
    a = int(input())
    A.append(a)
    if a == 0:
        break

A = A[::-1]
for i in range(len(A)):
    print(A[i])
