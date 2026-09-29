quantidade = 0
total = 0
maior = 0

while True:
    numero = float(input("Digite o número: "))

    if numero == 0:
            break

    if numero < 0:
        print("Numero invalido.")
    else:
        quantidade += 1
        total += numero
    
    if numero > maior:
        maior = numero

media = total / quantidade


print(f"Quantidade de vendas: {quantidade}")
print(f"Total de vendas: {total:.2f}")
print(f"Maior venda: {maior:.2f}")
print(f"Media de vendas: {media:.2f}")