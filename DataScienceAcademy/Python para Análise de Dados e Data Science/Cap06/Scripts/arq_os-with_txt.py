import os
#print(os.getcwd())

texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto += "Esses profissionais precisam saber como programar em Python.\n"
texto = texto + "E, claro, devem ser proficientes em Data Science."

# print(texto)
# arquivo = open(os.path.join('arquivos/cientista.txt'), 'w')

# for palavra in texto.split():
#     arquivo.write(palavra + ' ')

# arquivo.close()

# arquivo = open('arquivos/cientista.txt', 'r')
# conteudo = arquivo.read()
# arquivo.close()
# print(conteudo)

'''
A função with open é um modo mais seguro de trabalhar com arquivos, pois não é preciso chamar o close().
Em resumo o método close() é executado automaticamente.
'''
# with open('arquivos/cientista.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
# print(len(conteudo))
# print(conteudo)

# with open('arquivos/cientistas.txt', 'w') as arquivo:
#     arquivo.write(texto[:19])
#     arquivo.write('\n')
#     arquivo.write(texto[28:66])

arquivo = open('arquivos/cientistas.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
