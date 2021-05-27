nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:  "))
m = (nota1 + nota2) / 2
if m >= 6:
    print("Sua média foi boa")
else:
    print("Reprovado")
print("A sua média foi {:.1f}".format(m))
