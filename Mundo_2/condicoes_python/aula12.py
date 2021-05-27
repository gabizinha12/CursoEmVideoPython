nome = str(input("Qual o seu nome? "))
if nome == 'Alexandre':
    print("Que nome bonito")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome é bem popular")
else:
    print("Tenha um bom dia {}".format(nome))
