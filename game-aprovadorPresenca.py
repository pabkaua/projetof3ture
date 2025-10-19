def aprovar(stringAta, dicionario): # aprova o preenchimento da ata
    FILE = dicionario["ataAprovados"]
    with open(FILE, "a") as doc:
        doc.write(stringAta)

def refazerAta(listaNomes, dicionario): # refaz a ata escrevendo os nomes dos que foram pulados/não avaliados
    FILE = dicionario["ataGeral"]
    with open(FILE, "w") as doc:
        for linha in listaNomes:
            doc.write(linha)

def main(dicio): # confere se algum nome já esta preenchido, se não, executa as funções
    ata = dicio["ataGeral"]
    aprovados = dicio["ataAprovados"]
    listaAprovados = []
    listaAta = []
    confere = 0

    print("---- Aprovar presenças ----\n")

    try: # vai passar todos os aprovados para uma lista1
        with open(aprovados, 'r') as aprovadosTxt:
            for linha in aprovadosTxt:
                listaAprovados.append(linha.strip())
        confere += 1
    except FileNotFoundError:
        print("Arquivo de aprovados não encontrado! Será criado um novo\n")
        confere += 1


    try: # vai passar todos da ata para uma lista2
        with open(ata, "r") as ataTxt:
            for linha in ataTxt:
                listaAta.append(linha)
        confere += 1
    except FileNotFoundError:
        print("Arquivo de ata não encontrado!\n")
    

    if confere == 2: # se der tudo certo em passar para as listas
        sair = False
        novaAta = []
        index = -1
        for linha in listaAta:
            index += 1
            if linha.strip() not in listaAprovados:
                while sair == False:

                    status = input(linha.strip() + " - APROVAR[1] NÃO APROVAR[2] PULAR[3] SAIR [0]: ")
                    if status == "1":
                        aprovar(linha, dicio)
                        break
                    elif status == "2":
                        break
                    elif status == "3":
                        novaAta.append(linha)
                        break
                    elif status == '0': 
                        sair = True
                        break
                    else: 
                        print("Digite um número válido")

            if sair: 
                linhas_restantes = listaAta[index:]
                novaAta.extend(linhas_restantes)
                break
    refazerAta(novaAta, dicio)

dados = {
    "ataGeral": "game-ataPresenca.txt",
    "ataAprovados": "game-ataAprovados.txt"
}

main(dados)