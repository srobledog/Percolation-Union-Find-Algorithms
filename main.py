from QuickUnion import QuickUnion

def main():
    N = 10
    uf = QuickUnion(N)
    print(uf.parent)
    uf.union(0, 1)
    uf.union(4, 9)
    uf.union(6, 7)
    uf.union(1, 6)
    print(uf.parent)


if __name__ == '__main__':
    main()