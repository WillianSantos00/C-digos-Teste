valor1 = 0

valor2 = 1

lista = [valor1, valor2]

contador = 0


while contador < 10:

    lista.append(lista[-1]+lista[-2])
    contador += 1


num = int(input("Digite um número até 89 para verificar se ele faz parte da sequência de Fibonacci \n"))


if num not in lista:
    print(f"O valor digitado não está na sequência de Fibonacci {lista}")
else:
    print("O valor digitado está na sequência de Fibonacci")


