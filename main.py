from WeightedQuickUnion import WeightedQuickUnion
from WeightedQuickUnionPC import WeightedQuickUnionPC
from QuickUnion import QuickUnion
from QuickFind import QuickFind
import time
import numpy
from matplotlib import pyplot

def main():
    N = 1000
    unions_arr = numpy.arange(0, 2000, 20)
    trials = 100

    pyplot.figure()
    for kind in [WeightedQuickUnion, WeightedQuickUnionPC]:
        times = []
        std = []
        for amount in unions_arr:
            times_arr = []
            for _ in range(trials):
                uf = kind(N)
                start = time. time()
                
                for _ in range(amount):
                    uf.union(numpy.random.randint(N), numpy.random.randint(N))
                    uf.connected(numpy.random.randint(N), numpy.random.randint(N))
                end = time. time()
                print(kind.__name__, amount, end - start)
                times_arr.append(end - start)

            times.append(numpy.mean(times_arr))
            std.append(numpy.std(times_arr))

        pyplot.plot(unions_arr, times, "-o", label=kind.__name__)
        pyplot.errorbar(unions_arr, times, yerr=std, fmt="none", ecolor="black")
    
    pyplot.legend(loc="best")        
    pyplot.savefig("mientras.pdf")
    pyplot.close()









if __name__ == '__main__':
    main()