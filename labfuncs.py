#all required functions are in this file
def read_file(file_name):
    import csv
    tsv_file = open(file_name)
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    x = []
    y = []
    n = 0
    for row in read_tsv:
        x.append(float(row[0]))
        y.append(float(row[1]))
        n += 1
    return x, y, n


def product(a,b):
    return a*b


def mean(lst, count):
    return sum(lst)/count


def calc_m(xySum, nYX, xSquareSummed, n, xMeanSquared):
    m = (xySum - nYX) / (xSquareSummed - n * xMeanSquared)
    return m


def calc_c(m, ymean, xmean):
    return ymean - (m * xmean)


def calc_predicted(m, x_lst, c, size):
    y_predicted = []
    for i in range(0, size):
        temp = m * x_lst[i] + c
        y_predicted.append(temp)
    return y_predicted


def calc_error(m, x, c, actual_y, size):
    predicted_y = calc_predicted(m, x, c, size)
    error = []
    for i in range(0, size):
        temp = predicted_y[i] - actual_y[i]
        error.append(temp)

    error_squared = list(map(lambda a: a * a, error))

    mse = mean(error_squared, size)
    return mse
