from random import randint
num = int(input("Adivinhe um número:  "))
escolha = randint(0,5)
if num != escolha:
    print("Você perdeu")
else:
    print("Você ganhou")