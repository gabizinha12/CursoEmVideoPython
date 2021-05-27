salario = float(input("Digite seu salário: R$  "))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)

print("Quem ganhava {:.2f}, passa a ganhar {:.2f} agora".format(salario, aumento))

