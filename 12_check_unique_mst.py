class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra
        return True

def kruskal(n, edges, skip_edge=None):
    dsu = DSU(n)
    mst = []
    total = 0
    for edge in sorted(edges, key=lambda x: x[2]):
        if edge == skip_edge:
            continue
        u, v, w = edge
        if dsu.union(u, v):
            mst.append(edge)
            total += w
        if len(mst) == n - 1:
            break
    if len(mst) != n - 1:
        return None, float('inf')
    return mst, total

def check_unique_mst(n, edges, given_mst):
    given_weight = sum(w for _, _, w in given_mst)
    base_mst, base_weight = kruskal(n, edges)
    if base_weight != given_weight:
        return False, base_mst, base_weight
    for edge in given_mst:
        new_mst, new_weight = kruskal(n, edges, skip_edge=edge)
        if new_weight == given_weight:
            return False, new_mst, new_weight
    return True, given_mst, given_weight

edges1 = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
given_mst1 = [(2,3,4),(0,3,5),(0,1,10)]
edges2 = [(0,1,1),(0,2,1),(1,3,2),(2,3,2),(3,4,3),(4,2,3)]
given_mst2 = [(0,1,1),(0,2,1),(1,3,2),(3,4,3)]
print(check_unique_mst(4, edges1, given_mst1))
print(check_unique_mst(5, edges2, given_mst2))
