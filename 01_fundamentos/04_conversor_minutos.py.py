tempo = int(input("Quantidade em minutos: "))

horas = tempo // 60
minutos = tempo % 60

print(f"Dá {horas}h e {minutos:.2f}min")