class WeightedQuickUnionPC:
    def __init__(self, N):
        self.N = N
        self.parent = list(range(N))
        self.rank = [0 for _ in range(N)]

    def root(self, i):
        if i == self.parent[i]:
            return i

        r = self.root(self.parent[i])
        self.parent[i] = r
        return r

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        
        if (i == j):
            return

        if (self.rank[i] < self.rank[j]):
            self.parent[i] = j
        elif (self.rank[i] > self.rank[j]):
            self.parent[j] = i
        else:
            self.parent[i] = j
            self.rank[j] += 1