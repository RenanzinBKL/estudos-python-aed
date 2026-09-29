nota = float(input("Nota: "))

if nota >= 0 and nota <= 10:
    if nota >= 7 and nota <= 10:
        print("Aprovado.")
    elif nota >= 4 and nota < 7:
        print("Recuperação.")
    else:
        print("Reprovado.")
else:
    print("Nota Invalida.")