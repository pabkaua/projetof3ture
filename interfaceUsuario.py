import CRUD 
from logger import lerArquivoAluno, lerArquivoProfessor

dadosAlunos = {}
dadosProfessor = {} 

def menu(dadosAlunos, dadosProfessor):
    programa = 1
    while programa == 1:
        print("Seja bem vindo ao sistema da F3 Fitness. Digite:")
        print("1 - Cadastrar alunos ou professor")
        print("2 - Ver dados dos usuários do sistema")
        print("3 - Atualizar dados de Cadastro")
        print("4 - Remover usuário do sistema")
        print("5 - Ver todos os produtos fornecidos pela F3 Fitness")
        print("0 - Fechar programa")
        escolha = int(input("Escolha o que você deseja fazer: "))
        print("\n")
           
        if escolha == 0:
            print("Programa encerrado")
            programa = 0
            return dadosAlunos, dadosProfessor
        
        elif escolha == 1:
            dadosAlunos, dadosProfessor = CRUD.create(dadosAlunos, dadosProfessor)
        
        elif escolha == 2:
            CRUD.read(dadosAlunos, dadosProfessor)
                
        elif escolha == 3:
            CRUD.update(dadosAlunos, dadosProfessor)
                
        elif escolha == 4:
            CRUD.delete(dadosAlunos, dadosProfessor)
            
        elif escolha == 5:
            print("Os nossos produtos com os respectivos valores são:")   
            print("Plano MENSAL - R$ 90.00") 
            print("Plano TRIMESTRAL - R$ 260.00")
            print("Plano SEMESTRAL - R$ 500.00")
            print("Plano ANUAL - R$ 950.00")
            print("\n")        
        else:
            escolha = int(input("Entrada inválida. Tente novamente: "))

dadosAlunos = lerArquivoAluno(dadosAlunos)
dadosProfessor = lerArquivoProfessor(dadosProfessor)

dadosAlunos, dadosProfessor = menu(dadosAlunos, dadosProfessor)



        
    
    
    

      
    
