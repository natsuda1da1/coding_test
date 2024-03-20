H, W = map(int, input().split())
h, w = map(int, input().split())

white = H*W
black = W*h + H*w - h*w

print(white - black)