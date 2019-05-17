from src.WeightedQuickUnion import WeightedQuickUnion
from src.QuickUnion import QuickUnion
import time
import numpy
from matplotlib import pyplot

def main():
    N = 2000
    unions_arr = numpy.arange(0, N + N // 40, N // 40)
    trials = 200

    pyplot.figure()
    for kind in [QuickUnion, WeightedQuickUnion]:
        times = []
        std = []
        for amount in unions_arr:
            times_arr = []
            print(kind.__name__, amount)
            for _ in range(trials):
                uf = kind(N)
                start = time. time()
                
                for _ in range(amount):
                    uf.union(numpy.random.randint(N), numpy.random.randint(N))
                    # uf.connected(numpy.random.randint(N), numpy.random.randint(N))
                end = time. time()
                times_arr.append(end - start)

            times.append(numpy.mean(times_arr))
            std.append(numpy.std(times_arr))

        pyplot.plot(unions_arr, times, "-o", label=kind.__name__)
        # pyplot.errorbar(unions_arr, times, yerr=std, fmt="none", ecolor="black")
    
    pyplot.ylim(0)
    pyplot.grid()
    pyplot.legend(loc="best")
    pyplot.xlabel(r"$\rm Union \ cycles$", fontsize=30)
    pyplot.ylabel(r"$\rm time \ [\rm seconds]$", fontsize=30)
    pyplot.tight_layout()
    pyplot.savefig("union-times.pdf")
    pyplot.close()









if __name__ == '__main__':
    main()