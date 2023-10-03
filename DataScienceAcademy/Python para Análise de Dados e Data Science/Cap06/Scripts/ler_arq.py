arq1 = 'C:/Users/Matheus Gomes/Desktop/Análise de Dados/DataScienceAcademy/Python para Análise de Dados e Data Science/Cap06/arquivos/arquivo1.txt'
arq1 = open(arq1, 'r')
print(type(arq1))  # retorna o tipo '_io.TextIOWrapper'
print(arq1.read())  # ao ler um arquivo, o interpretador leva o cursor para o final do arquivo,
print(arq1.read())  # caso chame a leitura novamente vai mostra texto em branco
print(arq1.seek(0, 0))  # com o método seek podemos voltar ao inicio do arquivo passando as coordenadas
print(arq1.read(23))  # faz a leitura do arquivo até o caractere 23
print(arq1.read())  # faz a leitura do restante do arquivo de onde o cursou parou, no caso 23 para frente



