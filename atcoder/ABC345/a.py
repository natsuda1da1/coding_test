S = input()

for i in range(len(S)):
    if i == 0:
        if S[i] != "<":
            print("No")
            break
    elif i == len(S)-1:
        if S[i] != ">":
            print("No")
            break
    else:
        if S[i] != "=":
            print("No")
            break
else:
    print("Yes")