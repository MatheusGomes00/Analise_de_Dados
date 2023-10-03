import math

def cond_lista(lista):
    return sorted(list(map(int, lista.split())))


def desvio_padrao(lista): # Desvio padrão de uma amostra  stats.stdev(lista_tratada) --> desvio padrão amostral dos dados
    lista_tratada = cond_lista(lista)
    media = sum(lista_tratada) / len(lista_tratada)
    soma_quadrados = 0
    for valor in lista_tratada:
        diferenca = valor - media  # desvios
        soma_quadrados += diferenca ** 2
    desvio_padrao = math.sqrt(soma_quadrados / (len(lista_tratada) -1))
    print(f"Desvio padrão: {desvio_padrao:.2f}")


lista = "3 4 5 6 7"
desvio_padrao(lista)
