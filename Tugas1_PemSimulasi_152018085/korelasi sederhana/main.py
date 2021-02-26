import data
import pearsoncorrelation


def main():
    print("-------------------------")
    print("Fikri Haekal")
    print("152018085")
    print("tugas 1 pemograman simulasi ")
    print("-------------------------")

    independent = []
    dependent = []

    for d in range(1, 4):

        if data.populatedata(independent, dependent, d) == True:

            rho = pearsoncorrelation.pearson_correlation(independent, dependent)

            print("Dataset %d\n---------" % d)
            print("Independent data: " + (str(independent)))
            print("Dependent data:   " + (str(dependent)))
            print("Pearson Correlation Coefficient rho = %1.2f\n" % rho)
        else:
            print("Cannot populate Dataset %d" % d)


main()
