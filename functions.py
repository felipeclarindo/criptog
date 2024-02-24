import os
import platform


def fazer_login(user, password):
    db = {
        "Felipe": "123"
    }
    if user in db and password == db[user]:
        return "Logado!"
    elif user in db and db[user] != password:
        return "Senha inválida!"
    else:
        return "Não cadastrado!"


def criptografar(palavra, chave = [ "0x01", "0x02", "0x03", "0x04", "0x05", "0x06", "0x07", "0x08", "0x09", "0x0A", 
"0x0B", "0x0C", "0x0D", "0x0E", "0x0F", "0x10", "0x11", "0x12", "0x13", "0x14", 
"0x15", "0x16", "0x17", "0x18", "0x19", "0x1A", "0x1B", "0x1C", "0x1D", "0x1E", 
"0x1F", "0x20", "0x21", "0x22", "0x23", "0x24", "0x25", "0x26", "0x27", "0x28", 
"0x29", "0x2A", "0x2B", "0x2C", "0x2D", "0x2E", "0x2F", "0x30", "0x31", "0x32", 
"0x33", "0x34", "0x35", "0x36", "0x37", "0x38", "0x39", "0x3A", "0x3B", "0x3C", 
"0x3D", "0x3E", "0x3F", "0x40", "0x41", "0x42", "0x43", "0x44", "0x45", "0x46", 
"0x47", "0x48", "0x49"]
):  

    algarismos = "abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV1234567890,!@#$%^&*()-_+="
    palavra_criptografada = ""

    for letra in palavra:
        indice = algarismos.index(letra)
        palavra_criptografada += chave[indice]

    return palavra_criptografada

def desencriptografar(palavra, chave=list):

    intervalo = len(chave[0])

    algarismos = "abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV1234567890,!@#$%^&*()-_+="
    palavra_desencriptografada = ""

    for c in range(0, len(palavra), intervalo):
        valor = palavra[c:c+4]
        
        indice = chave.index(valor)
        palavra_desencriptografada += algarismos[indice]

    return palavra_desencriptografada


def clear_terminal()-> None:
    print(platform.system())
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        print("PlataformaAAA indefinida!")

def banner():
    clear_terminal()
    print("""\033[1;32m       
  _____      _       _         _____          
 / ____|    |_|     | |       / ____|         
| |     _ __ _ _ __ | |_ ___ | |  __          
| |    | '__| | '_ \| __/ _ \| | |_ |         
| |____| |  | | |_) | || (_) | |__| |         
 \_____|_|  |_|_.__/ \__\___/ \_____|         
            | |            𝚋̷𝚢̷ 𝙵̷𝚎̷𝚕̷𝚒̷𝚙̷𝚎̷        
            |_|                        \033[0m""")


if __name__ == "__main__":
    pass