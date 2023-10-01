"""
    É o grau de achatamento de uma distribuição, em relação a distribuição normal.
    A curtose pode ser de três tipos:
    Mesocúrtica - quando a distribuição é normal.
    Leptocúrtica - quando a distribuição é mais pontiaguda que a normal.
    Platicúrtica - quando a distribuição é mais achatada que a normal.

    Coeficiente percentílico de curtose:
    
        C = (Q3-Q1)/2(P90-P10)
    
    Se C = 0,263 a distribuição é Mesocúrtica
    Se C < 0,263 a distribuição é Leptocúrtica
    Se C > 0,263 a distribuição é Platicúrtica
"""
from scipy.stats import kurtosis
import numpy as np


def cond_lista(lista):
    return sorted(list(map(int, lista.split())))


def percentil(lista, n_percent):
    position = int(len(lista) * (n_percent/100)) - 1
    # print(f"Percentil {n_percent} = {lista[position - 1]}")
    return lista[position]


def coeficiente_per_curt(lista):  # coeficiente percentílico de curtose
    lista_tratada = cond_lista(lista)
    posit_q_1 = int(len(lista_tratada) * 0.25) - 1  # Q1
    posit_q_3 = int(len(lista_tratada) * 0.75) - 1 # Q3
    quartil_1 = lista_tratada[posit_q_1]
    quartil_3 = lista_tratada[posit_q_3]
    percentil_90 = percentil(lista_tratada, 90)
    percentil_10 = percentil(lista_tratada, 10)    
    curtose = (quartil_3 - quartil_1) / (2 * (percentil_90 - percentil_10))
    distribuicao = ''
    if curtose == 0.263:
        distribuicao = "Mesocúrtica"
    if curtose < 0.263:
        distribuicao = "Leptocúrtica"
    if curtose > 0.263:
        distribuicao = "Platicúrtica"
    print(f"Coeficiente Percentílico de Curtose: {curtose:.2f}\nDistribuição {distribuicao}\n")


def curtose_pearson(lista):
    lista_tratada = cond_lista(lista)
    curtose = kurtosis(lista_tratada)
    curt_fisher = kurtosis(lista_tratada, fisher=False)
    print(f"Coeficiente de Curtose Pearson com correção de Fisher:: {curtose:.2f}")
    print(f"Coeficiente de Curtose Pearson sem correção de Fisher: {curt_fisher:.2f}")


if __name__ == "__main__":
    lista = "240 240 240 240 255 255 255 280 240 240 240 240 280 290 390 300 255 255 255 280 300 300 300 300"
    coeficiente_per_curt(lista)
    curtose_pearson(lista)
