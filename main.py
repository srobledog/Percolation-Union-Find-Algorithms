from WeightedQuickUnionPC import WeightedQuickUnionPC

def main():
    N = 10
    uf = WeightedQuickUnionPC(N)

    uf.union(3, 8)
    uf.union(6, 8)
    uf.union(9, 4)
    uf.union(2, 1)
    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)
    uf.union(6, 1)
    # uf.union(7, 3)

    print(uf.parent)
    print(uf.size)

if __name__ == '__main__':
    main()