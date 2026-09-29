usuario = str(input("Úsuario: "))
senha = float(input("Senha: "))

if usuario == "admin" and senha == 1234:
    print("Login realizado.")
else:
    print("Usuário ou senha incorretos.")