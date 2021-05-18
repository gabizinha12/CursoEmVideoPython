salario = float(input("Digite o salário: \nR$"))
aumento = salario * 15 / 100
print("O salário do funcionário que era de R${:.2f} agora será de R${:.2f} com o aumento de 15%".
      format(salario, aumento + salario))
