import pandas as pd
dataset = 'C:/Users/Matheus Gomes/Desktop/Análise de Dados/DataScienceAcademy/Python para Análise de Dados e Data Science/Cap06/arquivos/salarios.csv'
data_frame = pd.read_csv(dataset)
print(data_frame.head())
print(data_frame['Position Title'].value_counts())
