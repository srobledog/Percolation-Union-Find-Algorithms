from .WeightedQuickUnion import WeightedQuickUnion
import numpy


class Percolation:
    def __init__(self, L):
        self.L = L
        self.sites = numpy.zeros((L, L), dtype=bool)
        self.opened = 0

        self.uf = WeightedQuickUnion(L * L + 2)

        self.top = L * L
        self.bottom = L * L + 1


    def getIndex(self, i, j):
        return j * self.L + i


    def isOpen(self, i, j):
        return self.sites[i, j]


    def open(self, i, j):
        if not self.sites[i, j]:
            index = self.getIndex(i, j)

            self.opened += 1

            self.sites[i, j] = True

            if (j == 0):
                self.uf.union(index, self.top)

            if (j == (self.L - 1)):
                self.uf.union(index, self.bottom)

            # left
            if (j > 0) and self.isOpen(i, j - 1):
                self.uf.union(index, self.getIndex(i, j - 1))

            # right
            if (j < (self.L - 1)) and self.isOpen(i, j + 1):
                self.uf.union(index, self.getIndex(i, j + 1))

            # up
            if (i > 0) and self.isOpen(i - 1, j):
                self.uf.union(index, self.getIndex(i - 1, j))

            # down
            if (i < (self.L - 1)) and self.isOpen(i + 1, j):
                self.uf.union(index, self.getIndex(i + 1, j))


    def connectedToTop(self, i, j):
        return self.uf.connected(self.getIndex(i, j), self.top)


    def numberOfOpenSites(self):
        return self.opened


    def percolates(self):
        return self.uf.connected(self.top, self.bottom)