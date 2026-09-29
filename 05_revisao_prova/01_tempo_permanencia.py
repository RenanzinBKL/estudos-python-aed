hora_entrada = int(input("Hora de entrada: "))
min_entrada = int(input("Minuto de entrada: "))

hora_saida = int(input("Hora de saida: "))
min_saida = int(input("Minuto de saida: "))

entrada = hora_entrada * 60 + min_entrada
saida = hora_saida * 60 + min_saida

total = saida - entrada

print(f"Foram {total} minutos totais.")
print(f"Sendo {total // 60}h {total % 60}min.")