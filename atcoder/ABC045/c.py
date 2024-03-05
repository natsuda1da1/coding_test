#not yet

S = input()

sm = 0
patterns = [int(S)]
for bit in range(1 << len(S)-1):
    tmp = []
    for i in range(1, len(S)-1):
        if bit & (1 << i):
            tmp.append(int(S[-(2*i+1):-1]))
    print(tmp)

    
    
            

