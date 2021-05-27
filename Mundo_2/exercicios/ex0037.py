n = int(input("Digite o número que deseja converter:  "))
print('Escolha uma das bases para conversão'
      '[1] Converter para binário'
      '[2] Converter para octal'
      '[3] Converter para hexadecimal')

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f'"{n} convertido para binário é igual a {bin(n)[2:]}"')
elif opcao == 2:
    print(f'"{n} convertido para octal é igual a {oct(n)[2:]}"')
elif opcao == 3:
    print(f'"{n} convertido para hexadecimal é igual a {hex(n)[2:]}"')

