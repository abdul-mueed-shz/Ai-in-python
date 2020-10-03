from labfuncs import *
#imports functions written by me from labfuncs py file

def main():
    file1 = "D:\houseSales.tsv"
    house_x, house_y, house_n = read_file(file1)
    house_m, house_c = calculate(house_x, house_y, house_n)
    house_mse = calc_error(house_m, house_x, house_c, house_y, house_n)

    print('For houseSales.tsv Value of m is {} and c is {}'.format(house_m, house_c))
    print('MSE for houseSales.tsv is {}'.format(house_mse), '\n')

    file2 = "D:\dollar.tsv"
    dollar_x, dollar_y, dollar_n = read_file(file2)
    dollar_m, dollar_c = calculate(dollar_x, dollar_y, dollar_n)
    dollar_mse = calc_error(dollar_m, dollar_x, dollar_c, dollar_y, dollar_n)


    print('For dollar.tsv Value of m is {} and c is {}'.format(dollar_m, dollar_c))
    print('MSE for dollar.tsv is {}'.format(dollar_mse))




def calculate(x, y, n):
    xy_sum = 0
    for i in range(0, n):
        xy_sum = xy_sum + product(x[i], y[i])

    y_mean = mean(y, n)
    x_mean = mean(x, n)
    nyx = n*x_mean*y_mean
    squared_xmean = product(x_mean, x_mean)

    xsquared_summed = 0
    for i in range(0, n):
        xsquared_summed = xsquared_summed + product(x[i], x[i])

    m = calc_m(xy_sum, nyx, xsquared_summed, n, squared_xmean)
    c = calc_c(m, y_mean, x_mean)

    return m, c



main()
