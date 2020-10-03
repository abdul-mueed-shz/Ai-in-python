from labfuncs import *
#importing written func by me from labfuncs

def main():
    filename = "D:\houseSales.tsv"
    outputfilename = "House-SalesDataReport.txt"
    #calc(filename, 0.00, -10, 0.01, 0.05, 0.50, 10, outputfilename)
    filename2 = "D:\dollar.tsv"
    calc(filename2, 0.00, -6000, 0.01, 0.05, 5, -4000, "dollars.txt")


def calc(filename, M, C, mincrement, cincrement, msize, csize, outputfilename):
    file1 = filename
    x, y, n = read_file(file1)
    out = open(outputfilename, 'w')
    m_least = 0
    c_least = 0
    m = M  # 0.00
    c = C  # -10
    m_increment = mincrement  # 0.01
    c_increment = cincrement  # 0.05
    m_size = msize  # 0.50
    c_size = csize  # 10
    least = 100000000000000000000000
    while m < m_size:
        while c < c_size:
            i = 0
            error = 0
            while i < n:
                predicted = 0
                temp = 0
                predicted = m * x[i] + c
                temp = predicted - y[i]
                temp = temp * temp
                error += temp
                i += 1
            mse = error / n
            #out.write("mse: {} \t m: {} \t c: {}".format(round(least, 3), round(m, 2), round(c, 2)))
            #out.write('\n')
            if mse < least:
                m_least = m
                c_least = c
                least = mse
            c += c_increment
        m += m_increment
        c = C

    out.write("\n\nThe Least MSE is {}, Least m is {}, Least c is {}".format(least, m_least, c_least))
    out.close()

    print("\nm least", m_least)
    print("c least", c_least)
    print("least mse", least)


main()
