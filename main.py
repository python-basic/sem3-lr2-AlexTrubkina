import math
def main():
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    c = float(input("Введите с: "))
    res = grn(a, b, c)
    print(res)


def grn(a, b, c):
    ppr = (a+b+c) / 2
    pl = sqrt(ppr * (ppr-a) * (ppr-b) * (ppr-c))
    return pl
