class QuickUnion:
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]

    def root(self, i):
        while (i != self.parent[i]):
            i = self.parent[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.parent[i] = j