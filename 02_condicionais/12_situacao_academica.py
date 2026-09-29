media = float(input("Média: "))
frequencia = float(input("Frequência: "))

if media >= 7 and frequencia >= 75:
    print("Aprovado")
elif media >= 7 and frequencia < 75:
    print("Reprovado por falta")
elif media < 7 and frequencia >= 75:
    print("Reprovado por nota")
else:
    print("Reprovado por nota e falta")