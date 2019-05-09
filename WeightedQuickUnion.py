class WeightedQuickUnion:
    def __init__(self, N):
        self.N = N
        self.id = [i for i in range(N)]
        self.size = [1 for i in range(N)]

    def root(self, i):
        while (i != self.id[i]):
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        
        if (i == j):
            return

        if (self.size[i] < self.size[j]):
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]