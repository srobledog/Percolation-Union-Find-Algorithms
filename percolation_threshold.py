from src.Percolation import Percolation
from src.Plot import plot_lattice_percolation
import numpy

def main():
    L = 100
    trials = 100

    values = []
    for _ in range(trials):
        lattice = Percolation(L)
        while not lattice.percolates():
            i = numpy.random.randint(L)
            j = numpy.random.randint(L)
            lattice.open(i, j)

        values.append(lattice.numberOfOpenSites() / L**2)

    print(f"pc mean = {numpy.mean(values)}")
    print(f"pc std = {numpy.std(values)}")
    plot_lattice_percolation(lattice)

if __name__ == '__main__':
    main()