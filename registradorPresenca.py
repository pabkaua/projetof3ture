def preencherAta(dados): # adiciona na ultima linha da ata a presença do usuário
    nome = dados["nome"]
    data = dados["data"]
    FILE = dados["ata"]

    with open(FILE, "a") as arquivo:
        linha = f"{data} | {nome}\n"
        arquivo.write(linha)


def checarPreenchimento(dados): # checa se o usuário já preencheu a ata no dia
    nome = dados["nome"]
    hoje = dados["data"]
    FILE = dados["ata"]

    with open(FILE, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.split(" | ")
            dataAta = linha[0]
            nomeAta = linha[1].strip()
            if nome == nomeAta and hoje == dataAta:
                return True
    return False
            

def checarCodigo(dados): # checa se o código fornecido foi o mesmo da academia
    numeroEntrada = input("Digite o código do dia: ")
    if numeroEntrada == dados["codigo"]:
        retorno = True
    else:
        retorno = False
    return retorno


def presencaDoDia(dados): # menu do usuário
    nome = input("Qual seu nome completo?\n").upper()
    dados["nome"] = nome

    nomePrint = nome.split()
    nomePrint = nomePrint[0].capitalize()
    presenca = input(f"{nomePrint}, você foi a academia hoje? [s][n]\n")

    if presenca == "s":
        if not checarPreenchimento(dados):
            if checarCodigo(dados):
                preencherAta(dados)
                print("Registrado. Os pontos serão adicionados assim que o instrutor aprovar sua presença.\n")
            else:
                print("Código inválido!")
        else:
            print("Você já preencheu a ata hoje!")
    else:
        print("Ok. Presença não registrada")


# main
from datetime import date
# from interfaceUsuario import codigo
ATA_FILE = "ataPresenca.txt"

data_hoje = date.today()
codigo_dia = "1"

dados = {
    "nome": "",
    "codigo": codigo_dia,
    "data": str(data_hoje),
    "ata": ATA_FILE
}
presencaDoDia(dados)