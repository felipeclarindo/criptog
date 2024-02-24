from functions import *


banner()
input("APERTE ENTER PARA CONTINUAR")

user = str(input("User> "))
passw = str(input("Password> "))
try:
    login = fazer_login(user, passw)

    if login == "Logado!":
        print("[1] Criptografar")
        print("[2] Desencriptografar")
        print("[3] Avisos")
        choice = int(input("Digite o desejado: "))
        if choice == 1:
            palavra = str(input("Digite a palavra ou texto que deseja criptografar!"))

        elif choice == 2:
            str(input("Digite a palavra ou texto que deseja desincriptografar em base nossa chave padrão."))
        elif choice == 3:
            print("Usamos nossa chave de criptografia, caso deseja usar outra troque-a. ")

    else:
        print("Acesso restrito!")

except Exception as e:
    print(f"Erro: {e}")
