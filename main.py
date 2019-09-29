
def main():
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    c = float(input("Введите с: "))
    if a+b > c and a > 0 and b > 0 and c > 0:
        if a+c > b:
            if b+c > a:
                res = grn(a, b, c)
            print(res)
    else: 
        print("Треугольника не существует")

import math
def grn(a, b, c):
    """
    Расчет площади треугольника по формуле Герона
    """
    ppr = (a+b+c) / 2
    pl = pow(ppr * (ppr-a) * (ppr-b) * (ppr-c), 0.5)
    return pl

main()
