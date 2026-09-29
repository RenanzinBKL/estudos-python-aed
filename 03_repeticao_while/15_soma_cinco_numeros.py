contador = 0
total = 0

while contador < 5:
    numero = float(input("Número: "))
    
    total += numero
    contador += 1 
    
print(f"A soma dá: {total}")