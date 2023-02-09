class QuickFind:
    def __init__(self, N):
        self.N = N
        self.id = list(range(N))
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.N):
            if self.id[i] == pid:
                self.id[i] = qid
