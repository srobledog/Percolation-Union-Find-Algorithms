class WeightedQuickUnion:
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]

    def root(self, i):
        while (i != self.parent[i]):
            i = self.parent[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        
        if (i == j):
            return

        if (self.size[i] <= self.size[j]):
            self.parent[i] = j
            self.size[j] += self.size[i]
        else:
            self.parent[j] = i
            self.size[i] += self.size[j]