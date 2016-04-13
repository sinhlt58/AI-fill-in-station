def ham_so(x, n):
    return x ** 10 - (n + 2) * x + n + 1


def dao_ham(x, n):
    return 10 * x ** 9 - n - 2


def get_ebf(n, error):
    # initial root
    xn = 2.0
    xn1 = xn - ham_so(xn, n) / dao_ham(xn, n)
    while abs(xn - xn1) > error:
        xn = xn1
        xn1 = xn - ham_so(xn, n) / dao_ham(xn, n)
    return xn1
