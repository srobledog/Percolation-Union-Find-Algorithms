from src.Lattice import Lattice
from src.Plot import plot_lattice
from itertools import product
from matplotlib import pyplot
from tqdm import tqdm
import numpy

def main():
    L = 100
    p = 0.5

    # lattice = Lattice(L)

    # sites = list(product(range(L), repeat=2))
    # numpy.random.shuffle(sites)
    
    # for site in sites[:int(p * L * L)]:
    #     lattice.open(*site)
    # plot_lattice(lattice)


    # other interesting result is to plot
    # the amount of clusters vs p
    amount_of_clusters = []
    p_arr = numpy.linspace(0, 1, 500)
    for p in tqdm(p_arr):
        lattice = Lattice(L)

        sites = list(product(range(L), repeat=2))
        numpy.random.shuffle(sites)
        
        for site in sites[:int(p * L * L)]:
            lattice.open(*site)

        _, amount = lattice.clusters()

        amount_of_clusters.append(amount)

    pyplot.figure()
    pyplot.plot(p_arr, amount_of_clusters, "+", ms=5)
    pyplot.grid()
    pyplot.xlabel("Site ocupation probability")
    pyplot.ylabel("Number of clusters")
    pyplot.tight_layout()
    pyplot.savefig("num_clusters_vs_p_.pdf")
    pyplot.close()





if __name__ == '__main__':
    main()