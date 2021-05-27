nota1 = float(input("Digite a primeira nota:  "))
nota2 = float(input("Digite a segunda nota:    "))
media = (nota1 + nota2) / 2
print(f'Tirando "{nota1}" e "{nota2}", sua média é de: "{media}"\033[m')

if media < 5.0:
    print("Abaixo da média, reprovado")
elif 7.0 > media >= 5.0:
    print("Em recuperação")
else:
    print("Está aprovado")
