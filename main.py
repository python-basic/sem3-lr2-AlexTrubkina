import math
def main():
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    c = float(input("Введите с: "))
    if a + b < c or a + c < b or b + c < a and a > 0 and b > 0 and c > 0:
        res = grn(a, b, c)
        print(res)
    else: 
        print("Треугольника не существует")


def grn(a, b, c):
    """
    Расчет площади треугольника по формуле Герона
    """
    ppr = (a+b+c) / 2
    pl = sqrt(ppr * (ppr-a) * (ppr-b) * (ppr-c))
    return pl
