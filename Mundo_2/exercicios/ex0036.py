nome = str(input("Qual seu nome? "))
casa = float(input("Qual o valor da casa?  "))
salario = float(input("Qual o seu salário?  "))
anos = int(input("Em quantos anos deseja parcelar?  "))


parcela = casa / (anos * 12)
minimo = salario * 30 / 100


if parcela <= minimo:
    print(f"A parcela é de {parcela:.2f} não excede 30% do seu salário")
    print("Parabéns seu empréstimo foi aprovado")
else:
    print(f"a parcela de {parcela:.2f} excede 30% do seu salário")
    print("Infelizmente seu empréstimo foi recusado")
