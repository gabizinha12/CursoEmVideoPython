val = int(input(("Digite um número para saber a tabuada: ")))
aux = 0
print("*" * 18)
print("Tabuada de {}".format(val))
print("*" * 18)
while aux <= 10:
    print("{0} X {1} = {2}".format(aux, val, (aux * val)))
    aux = aux + 1
