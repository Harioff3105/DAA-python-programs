class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    dsu = DSU(n)
    mst = []
    total = 0
    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total

print(kruskal(4, [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]))
print(kruskal(5, [(0,1,2),(0,3,6),(1,2,3),(1,3,8),(1,4,5),(2,4,7),(3,4,9)]))
