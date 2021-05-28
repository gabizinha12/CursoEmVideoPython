n1 = int(input("Primeiro segmento:  "))
n2 = int(input("Segundo segmento:  "))
n3 = int(input("Terceiro segmento:  "))


if n1 <= n2 + n3 and n2 <= n1 + n3 and n3 <= n1 + n2:
    print("Os segmentos formam um triângulo", end= '')
    if n1 == n2 == n3:
        print("Equilátero")
elif n1 != n2 != n3:
    print("Escaleno")
elif n1 == n2 != n3:
    print("Isósceles")
else:
    print("Os segmentos não formam um triângulo")
