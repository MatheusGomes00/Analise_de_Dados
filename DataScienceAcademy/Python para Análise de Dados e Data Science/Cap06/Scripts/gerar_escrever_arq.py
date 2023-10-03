arq2 = 'C:/Users/Matheus Gomes/Desktop/Análise de Dados/DataScienceAcademy/Python para Análise de Dados e Data Science/Cap06/arquivos/arquivo2.txt'
arq2 = open(arq2, 'r')  # abre o arquivo no modo leitura 
print(arq2.read())  # Aprendendo a programar em Python. E a metodologia de ensino da Data Science Academy facilita o aprendizado.
arq2.close()  # fecha o arquivo

arq2 = 'C:/Users/Matheus Gomes/Desktop/Análise de Dados/DataScienceAcademy/Python para Análise de Dados e Data Science/Cap06/arquivos/arquivo2.txt'
arq2 = open(arq2, 'w')  # abre o arquivo no modo escrita, se já existir sobrescreve, se não existir é criado no diretório especificado
arq2.write("Aprendendo sobre manipulação de arquivos com a DSA")  # sobrescreve o que já tiver escrito no arquivo
arq2.close()

# arq2 = 'C:/Users/Matheus Gomes/Desktop/Análise de Dados/DataScienceAcademy/Python para Análise de Dados e Data Science/Cap06/arquivos/arquivo2.txt'
# arq2 = open(arq2, 'r')
# print(arq2.read())  
# arq2.close()

# arq2 = 'C:/Users/Matheus Gomes/Desktop/Análise de Dados/DataScienceAcademy/Python para Análise de Dados e Data Science/Cap06/arquivos/arquivo2.txt'
# arq2 = open(arq2, 'a')  # abre o arquivo no modo append, adiciona ao final do arquivo
# arq2.write('\nJá passou de 1 hora, preciso mudar de atividade...')
# arq2.close

# arq2 = 'C:/Users/Matheus Gomes/Desktop/Análise de Dados/DataScienceAcademy/Python para Análise de Dados e Data Science/Cap06/arquivos/arquivo2.txt'
# arq2 = open(arq2, 'r')
# print(arq2.read())  
# arq2.seek(0,0)  # retorna o cursor apra o inicio do arquivo
# print(arq2.read())  
# arq2.close()
