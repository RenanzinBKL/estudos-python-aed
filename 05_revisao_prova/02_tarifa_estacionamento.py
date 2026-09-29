tipo = int(input("Tipo (1-Comum 2-Mensalista 3-Idoso/PCD): "))
tempo = int(input("Tempo de permanencia (min): "))

if tipo == 1:
    if tempo <= 15:
        print("Tarifa: Isento(tolerancia).")
    elif tempo <= 60:
        print("Tarifa: R$ 8") 
    elif tempo <= 180:
        print("Tarifa: R$ 15")
    else: 
        print("Tarifa: R$ 25")
        
if tipo == 2:
    print("Cliente mensalista: isento")

if tipo == 3:
    if tempo <= 15:
            print("Tarifa: Isento(tolerancia).")
    elif tempo <= 60:
            print("Tarifa: R$ 4") 
    elif tempo <= 180:
            print("Tarifa: R$ 7.5")
    else: 
            print("Tarifa: R$ 12.5")