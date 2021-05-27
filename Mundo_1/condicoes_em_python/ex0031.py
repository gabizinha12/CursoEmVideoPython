distancia = float(input("Digite a distância: "))
print("Você irá percorrer {}Km".format(distancia))
if distancia <= 200:
    passagem = distancia * 0.50
    print("O valor da sua passagem é {:.2f}".format(passagem))
else:
    passagem = distancia * 0.45
    print("O valor da sua passagem é {:.2f}".format(passagem))
