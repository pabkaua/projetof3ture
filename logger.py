LOG_FILE = 'dadosAcademiaAluno.txt'
LOG2_FILE = 'dadosAcademiaProfessor.txt'

def escreveCodigo():
    codigo = input("Cadastre o código de validação de presença: ")
    with open("gameCodigoDia.txt", "w") as codigoTxt:
        codigoTxt.write(codigo)
        print("Código cadastrado.\n")
    return codigo

def lerCodigo():
    with open("gameCodigoDia.txt", "r") as codigoTxt:
        codigo = codigoTxt.read().strip()
    return codigo

def salvarAlunoNoArquivo(dadosAlunos):
    with open(LOG_FILE, 'w') as arquivo:
        for nome, info in dadosAlunos.items():
            linha = f"aluno: {nome} | " + " | ".join([f"{chave}: {valor}" for chave, valor in info.items()])      
            arquivo.write(linha + "\n") 

def salvarProfessorNoArquivo(dadosProfessor):
     with open(LOG2_FILE, 'w') as arquivo2:
        for nome, info in dadosProfessor.items():
            linha = f"professor: {nome} | " + " | ".join([f"{chave}: {valor}" for chave, valor in info.items()]) 
            arquivo2.write(linha + "\n") 

def lerArquivoAluno(dadosAlunos):
    with open(LOG_FILE, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                partes = linha.split(" | ")
                dadoAluno = {}  
                nomeAluno = ''
                
                for p in partes:
                    chave, valor = p.split(":", 1)
                    chave = chave.strip()
                    valor = valor.strip()

                    if chave == "aluno":
                        nomeAluno = valor.upper() 
                    else:
                        dadoAluno[chave] = valor 

                    dadosAlunos[nomeAluno] = dadoAluno
    return dadosAlunos

def lerArquivoProfessor(dadosProfessor):
    with open(LOG2_FILE, "r") as arquivo2:
        for linha in arquivo2:
            linha = linha.strip()
            if linha:
                partes = linha.split(" | ")
                dadosProf = {}  
                nomeProf = ''
                
                for p in partes:
                    chave, valor = p.split(":", 1)
                    chave = chave.strip()
                    valor = valor.strip()

                    if chave == "professor":
                        nomeProf = valor.upper() 
                    else:
                        dadosProf[chave] = valor 

                
                    dadosProfessor[nomeProf] = dadosProf  

    return dadosProfessor

