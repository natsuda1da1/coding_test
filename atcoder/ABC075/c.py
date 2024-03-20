def root(parent, node):
    if parent[node] == node:
        return node
    return root(parent, parent[node])

def union(parent, rank, node1, node2):
    if rank[node2] > rank[node1]:
        parent[node1] = node2
        rank[node2] += 1
    else:
        parent[node2] = node1
        rank[node1] += 1


N, M = map(int, input().split())
E = tuple(tuple(map(int, input().split())) for _ in range(M))
ans = 0

for i in range(M):
    parent = [i for i in range(N+1)]
    rank = [0]*(N+1)
    for j in range(M):
        if i == j:
            continue
        x, y = E[j]
        parent_x = root(parent, x)
        parent_y = root(parent, y)
        if parent_x != parent_y:
            union(parent, rank, parent_x, parent_y)

    cnt = 0
    for k in range(1, N+1):
        if parent[k] == k:
            cnt += 1
            if cnt > 1:
                ans += 1
                break

print(ans)
