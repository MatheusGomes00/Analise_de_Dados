# abrir um arquivo em uma única linha, gerar uma lista
dataset = 'C:/Users/Matheus Gomes/Desktop/Análise de Dados/DataScienceAcademy/Python para Análise de Dados e Data Science/Cap06/arquivos/salarios.csv'
dataset = open(dataset, 'r')
data = dataset.read()
# print(data)
rows = data.split('\n')  # separa as linhas através da quebra de linha, gerando multip
# print(rows)
full_data = []
for row in rows:
    split_row = row.split(',')  # separa as colunas através da virgula, gerando várias listas
    full_data.append(split_row)
# print(full_data)  # o problema nesse procedimento está na separação dos nomes por virgula além das colunas
count = 0
for row in full_data:
    count += 1  # contagem das linhas
#print(count)
first_row = full_data[0]  # seleciona a primeira linha, que é uma lista
count2 = 0
for column in first_row:  
    count2 += 1  # contagem das colunas, é iterada a primeira linha que é uma lista
print(count2)

