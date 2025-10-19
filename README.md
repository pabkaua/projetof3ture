Funcionamento do código:

o main é responsável por receber a data do dia e guardar dentro de um dicionário, juntamente com o código de presença do dia - que será modificado todo dia
então, a função presencaDoDia é o menu, onde será impresso na tela do user se ele quer preencher a ata. Caso não queira, o programa termina automáticamente, 
caso queira, serão feitos - através da função checarCodigo e checarPreenchimento - testes se o código fornecido por ele é igual ao da academia no dia, e se 
ele já preencheu a ata nesse mesmo dia. Caso o código fornecido esteja correto, e ele não tenha preenchido a ata no mesmo dia, a função preencherAta é executada, 
adicionando no ataPresenca.txt a data e o nome do aluno/usuário.

execute jogo.py para registrar presença
execute validarPresenca.py para validar as presenças da ataPreseca.txt e gerar um ranking em ranking.txt
