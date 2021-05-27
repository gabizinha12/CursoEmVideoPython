from datetime import date
hoje = date.today().year
nasc = int(input("Digite a data de nascimento:  "))
idade = hoje - nasc
print(f"O atleta tem {idade} anos")

if idade <= 9:
    print("Classificação: MIRIM")
elif 9 < idade <= 14:
    print("Classificação: INFANTIL")
elif 14 < idade <= 19:
    print("Classificação: Junior")
elif 19 < idade <= 25:
    print("Classificação Sênior")
else:
    print("Master")