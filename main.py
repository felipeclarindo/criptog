from functions import *
from time import sleep


banner()
input("APERTE ENTER PARA VERIFICAÇÃO ")

while True: 
    banner()
    user = str(input("User> "))
    passw = str(input("Password> "))

    try:
        print("Fazendo login...")
        sleep(1)
        login = fazer_login(user, passw)

        if login == True:
            
            while True:
                banner()
                print("[1] Criptografar")
                print("[2] Desincriptografar")
                print("[3] Avisos")
                print("[4] Finalizar")
                choice = int(input("Digite o desejado: "))
                match choice:
                    case 1:
                        texto = str(input("Digite o que deseja criptografar: "))
                        texto_criptografado = criptografar(texto)
                        banner()
                        print(f"{texto} Criptografado:  {texto_criptografado}")
                        input("APERTE ENTER PARA CONTINUAR")
                        
                    case 2:
                        texto = str(input("Em base nossa chave padrão \nDigite o que deseja desincriptografar: "))
                        texto_desencriptografado = desincriptografar(texto)
                        banner()
                        print(f"{texto} Desencriptografado: {texto_desencriptografado}")
                        input("APERTE ENTER PARA CONTINUAR")
                        
                    case 3:
                        banner()
                        print("Usamos nossa chave de criptografia, caso deseja usar outra troque-a. ")
                        print("Desenvolvido por: Felipe Clarindo")
                        input("APERTE ENTER PARA CONTINUAR")
                    case 4:
                        banner()
                        print("Finalizado")
                        break
                    case _:
                        banner()
                        print("Opção Invalida!")
                        input("APERTE ENTER PARA CONTINUAR")
            break

        else:
            banner()
            print("Acesso restrito!")
            input("APERTE ENTER PARA CONTINUAR")

    except Exception as e:
        print(f"Erro: {e}")
