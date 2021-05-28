valor = int(input("Digite o valor das compras: "))
print("[1] á vista dinheiro/cheque"
      "[2] á vista cartão "
      "[3] 2x cartão"
      "[4] 3x ou mais no cartão")

opcao = int(input("Digite a opção:  "))

if opcao == 1:
    prc = valor * 10 / 100
    print(f"Você recebeu um desconto de 10% o valor agora é de R${valor - prc:.2f}")
elif opcao == 2:
    prc = valor * 5 / 100
    print(f"Você recebeu um desconto de 5% o valor agora é de R${valor - prc:.2f}")
elif opcao == 3:
    prc = valor + (valor * 20 / 100)
    vezes = int(input("Digite quantas vezes:  "))
    parcela = prc / vezes
    print(f'\nSua compra será parcelada em {vezes}x de R${parcela:.2f}')
    print(f'Com essa opção você tem 20 % de juros.. o valor final será: R${prc:.2f}')
else:
    print("Opção inválida")

