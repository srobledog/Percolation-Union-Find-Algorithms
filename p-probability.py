from src.Percolation import Percolation
from matplotlib import pyplot
from itertools import product
import numpy


def main():
    trials = 500
    p_arr = numpy.linspace(0, 1, 51)

    pyplot.figure()
    for L in [10, 20]:
    
        real_p_mean = []
        real_p_std = []

        percolation_probability_mean = []
        percolation_probability_std = []
        for p in p_arr:
            values = []
            fractions = []
            for _ in range(trials):
                lattice = Percolation(L)
                possible = list(product(range(L), repeat=2))
                numpy.random.shuffle(possible)
                while lattice.numberOfOpenSites() < (L * L * p):
                    i, j = possible[0]
                    possible.remove(possible[0])
                    lattice.open(i, j)
                
                values.append(lattice.percolates())
                fractions.append(lattice.numberOfOpenSites() / (L * L))

            percolation_probability_mean.append(numpy.mean(values))
            percolation_probability_std.append(numpy.std(values))

            real_p_mean.append(numpy.mean(fractions))
            real_p_std.append(numpy.std(fractions))

        pyplot.plot(real_p_mean, percolation_probability_mean, "-", lw=2, label=r"$L = %i$" % L)
        # pyplot.errorbar(real_p_mean, percolation_probability_mean, yerr=percolation_probability_std, fmt="none", ecolor="black")

    pyplot.grid()
    pyplot.legend(loc="best")
    pyplot.ylim(0, 1)
    pyplot.xlabel(r"$p$", fontsize=30)
    pyplot.ylabel(r"$\rm probability$", fontsize=30)
    pyplot.axhline(0.5, ls="--", color="crimson", lw=2)
    pyplot.axvline(0.59274605079210, ls="--", color="crimson", lw=2)
    pyplot.tight_layout()
    pyplot.savefig("percolation_probability.pdf")
    pyplot.close()

if __name__ == '__main__':
    main()