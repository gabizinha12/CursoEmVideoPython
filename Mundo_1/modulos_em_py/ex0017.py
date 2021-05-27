from math import hypot
c1 = float(input("Cateto Oposto: "))
c2 = float(input("Cateto adjacente: "))
hipo = hypot(c1, c2)
print("A hipotenusa é {:.2f}".format(hipo))
