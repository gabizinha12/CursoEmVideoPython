velocidade = float(input("Digite a velocidade do carro:  "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print("Você foi multado em {:.2f}, sua velocidade {} está acima do limite".format(multa, velocidade))
else:
    print("Você não foi multado")
