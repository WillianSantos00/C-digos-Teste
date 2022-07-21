
palavra = input("Digite uma palavra \n")

lista = list(palavra)

print(lista)

contador1 = 0
contador2 = len(lista)
contador3 = len(lista)
nova_lista = []

while contador1 < contador2:
    contador3 -= 1
    nova_lista.append(lista[contador3])

    contador1 += 1


print(f"Esta é sua palavra ao contrário: {nova_lista}")
