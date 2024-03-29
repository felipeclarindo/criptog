from os import name, system

# Caso queira usar outro modelo de criptografia, altere a chave padrão
chave_padrao = [ "0x01", "0x02", "0x03", "0x04", "0x05", "0x06", "0x07", "0x08", "0x09", "0x0A", 
"0x0B", "0x0C", "0x0D", "0x0E", "0x0F", "0x10", "0x11", "0x12", "0x13", "0x14", 
"0x15", "0x16", "0x17", "0x18", "0x19", "0x1A", "0x1B", "0x1C", "0x1D", "0x1E", 
"0x1F", "0x20", "0x21", "0x22", "0x23", "0x24", "0x25", "0x26", "0x27", "0x28", 
"0x29", "0x2A", "0x2B", "0x2C", "0x2D", "0x2E", "0x2F", "0x30", "0x31", "0x32", 
"0x33", "0x34", "0x35", "0x36", "0x37", "0x38", "0x39", "0x3A", "0x3B", "0x3C", 
"0x3D", "0x3E", "0x3F", "0x40", "0x41", "0x42", "0x43", "0x44", "0x45", "0x46", 
"0x47", "0x48", "0x49"]

# Adiciona o usuário neste dicionário para poder realizar o cadastro
db = {
    # "Nome" : "Senha":
}

def clear_terminal():
    # Verifica qual sistema operacional está sendo usado
    if name == 'posix':  # Para sistemas baseados em Unix (Linux, macOS)
        system('clear')
    elif name == 'nt':  # Para Windows
        system('cls')
    else:
        # Se o sistema operacional não for reconhecido, imprime uma mensagem de erro
        print("Sistema operacional não suportado.")


def fazer_login(user, password, db=db):
    # Verifica se o usuário e a senha correspondem ao registro no banco de dados
    if user in db and password == db[user]:
        return True
    else:
        return False

def criptografar(palavra, chave=["0x01", "0x02", "0x03", "0x04", "0x05", "0x06", "0x07", "0x08", "0x09", "0x0A",
"0x0B", "0x0C", "0x0D", "0x0E", "0x0F", "0x10", "0x11", "0x12", "0x13", "0x14",
"0x15", "0x16", "0x17", "0x18", "0x19", "0x1A", "0x1B", "0x1C", "0x1D", "0x1E",
"0x1F", "0x20", "0x21", "0x22", "0x23", "0x24", "0x25", "0x26", "0x27", "0x28",
"0x29", "0x2A", "0x2B", "0x2C", "0x2D", "0x2E", "0x2F", "0x30", "0x31", "0x32",
"0x33", "0x34", "0x35", "0x36", "0x37", "0x38", "0x39", "0x3A", "0x3B", "0x3C",
"0x3D", "0x3E", "0x3F", "0x40", "0x41", "0x42", "0x43", "0x44", "0x45", "0x46",
"0x47", "0x48", "0x49"]):

    algarismos = "abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV1234567890,!@#$%^&*()-_+="
    palavra_criptografada = ""

    # Criptografa a palavra usando a chave
    for letra in palavra:
        indice = algarismos.index(letra)
        palavra_criptografada += chave[indice]

    return palavra_criptografada

def desincriptografar(palavra, chave=["0x01", "0x02", "0x03", "0x04", "0x05", "0x06", "0x07", "0x08", "0x09", "0x0A",
"0x0B", "0x0C", "0x0D", "0x0E", "0x0F", "0x10", "0x11", "0x12", "0x13", "0x14",
"0x15", "0x16", "0x17", "0x18", "0x19", "0x1A", "0x1B", "0x1C", "0x1D", "0x1E",
"0x1F", "0x20", "0x21", "0x22", "0x23", "0x24", "0x25", "0x26", "0x27", "0x28",
"0x29", "0x2A", "0x2B", "0x2C", "0x2D", "0x2E", "0x2F", "0x30", "0x31", "0x32",
"0x33", "0x34", "0x35", "0x36", "0x37", "0x38", "0x39", "0x3A", "0x3B", "0x3C",
"0x3D", "0x3E", "0x3F", "0x40", "0x41", "0x42", "0x43", "0x44", "0x45", "0x46",
"0x47", "0x48", "0x49"]):

    intervalo = len(chave[0])

    algarismos = "abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV1234567890,!@#$%^&*()-_+="
    palavra_desencriptografada = ""

    # Descriptografa a palavra usando a chave
    for c in range(0, len(palavra), intervalo):
        valor = palavra[c:c+4]
        
        indice = chave.index(valor)
        palavra_desencriptografada += algarismos[indice]

    return palavra_desencriptografada

def banner():
    clear_terminal()
    # Imprime um banner na tela
    print("""\033[1;32m       
  _____      _       _         _____          
 / ____|    |_|     | |       / ____|         
| |     _ __ _ _ __ | |_ ___ | |  __          
| |    | '__| | '_ \| __/ _ \| | |_ |         
| |____| |  | | |_) | || (_) | |__| |         
 \_____|_|  | |_.__/ \__\___/ \_____| 
            | |        
            |_|            𝚋̷𝚢𝙵̷𝚎̷𝚕̷𝚒̷𝚙̷𝚎̷\033[0m""")

if __name__ == "__main__":
    banner()