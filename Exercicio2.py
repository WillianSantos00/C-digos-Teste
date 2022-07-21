faturamento_mensal = []

contador = 0
while contador < 30:
    num = int(input(f"Digite o número do faturamento do {contador+1}° dia \n R$"))
    faturamento_mensal.append(num)
    contador += 1


menor_faturamento = min(faturamento_mensal)
print(f"O menor faturamento do mês foi {menor_faturamento}")

maior_faturamento = max(faturamento_mensal)
print(f"O maior faturamento do mÊs foi {maior_faturamento}")

media_mensal = sum(faturamento_mensal)/30

lista_media = []
contador2 = 0
while contador2 < len(faturamento_mensal):
    if media_mensal > faturamento_mensal[contador2]:
        lista_media.append(faturamento_mensal[contador2])

    contador2 += 1

qnt_media = len(lista_media)

print(f'A quantidade de dias que o faturamento diário superou a média foi de {qnt_media}')



