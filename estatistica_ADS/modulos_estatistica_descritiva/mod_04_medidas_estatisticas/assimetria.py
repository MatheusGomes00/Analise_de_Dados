"""
    É o grau de desvio ou afastamento da simetria de uma distribuição. Quando a curva é simétrica,
    a média, a mediana e a moda coincidem, num mesmo ponto, de ordenada máxima, 
    havendo um perfeito equilibrio na distribuição. Quando o equilíbrio não acontece, isto é,
    a média, a mediana e a moda recaem em pontos diferentes da distribuição esta será assimétrica;
    enviesada a direita ou a esquerda.

    Distribuição simétrica     e    Assimétrica (S) = 0
        Mo = Me = |X                 Q3 - Me = Me - Q1

    Distribuição assimétrica Negativa ou enviesada a esquerda - quando os valores se concentram
    na extremidade superior da escala e se distribuem gradativamente em direção à extremidade
    inferior.
    Distribuição assimétrica Positiva ou enviesada a direita quando os valores se concentram na
    extremidade inferior da escala e se distribuem gradativamente em direção à extremidade 
    superior.
"""

import statistics as stats
# import math

def cond_lista(lista):
    return sorted(list(map(int, lista.split())))


def assimetria(lista):
    lista_tratada = cond_lista(lista)
    n = len(lista_tratada)
    media = stats.mean(lista_tratada)
    soma_cubos = 0
    for valor in lista_tratada:
        soma_cubos += ((valor - media) / stats.stdev(lista_tratada)) ** 3
    
    correcao = soma_cubos * (n / ((n-1) * (n-2)))
    print(f"Assimetria: {correcao:.2f}")

if __name__ == "__main__":
    lista = "240 240 240 240 255 255 255 280 240 240 240 240 280 290 390 300 255 255 255 280 300 300 300 300"
    assimetria(lista)
