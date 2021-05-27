from datetime import date

nasc = int(input("Digite a sua data de nascimento:   "))
hoje = date.today().year
idade = hoje - nasc

print(f"Quem nasceu em {nasc} tem {idade} anos {hoje}.")
if idade == 18:
    print("Você tem que se alistar imediatamente")
elif idade < 18:
    falta = 18 - idade
    print(f"Ainda faltam {falta} anos para seu alistamento")
    print(f"Seu alistamento será em {hoje + falta}")
elif idade > 18:
    foi = idade - 18
    print(f"Você já deveria ter se alistado em {foi} anos")
    print(f"Seu alistamento foi em {hoje - foi}")
