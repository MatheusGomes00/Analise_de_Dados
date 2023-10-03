"""
    > Média = usamos quando queremos encontrar 1 número que representa o conjunto de dados, a referência.
    (média aritmética simples é utilizada na tecnologia, a ponderada não);
    > Moda = o elemento que nais se repete em um conjunto de dados, o de maior frequência. 
    Amodal, modal, bimodal, trimodal;
    > Mediana = elemento central, divide o bando de dados na metade, e localiza o elemento central, 
    caso seja impar, encontra um centro, quando é par, pega os 2 centrais e calcula a média aritmética simples. 
"""

import statistics as stats
import sys
sys.stdout.reconfigure(encoding='utf-8')


lista = "25	26	29	20	22	24	25	25	25	26	26	27	28	28	28	28	29	29	20	20	23	24	25	26	27	27	28	29	29	30	31	36	36	36	38	38	41	42	45	57	58	52	56	58	45	25	26	28	29	36"

def cond_lista(lista):
    return sorted(list(map(int, lista.split())))


def calc_media(lista):
    lista = cond_lista(lista)
    media = stats.mean(lista)
    print(f"Média aritmética: {media:.2f}")


def calc_moda(lista):
    lista = cond_lista(lista)
    moda = stats.mode(lista)
    print(f"Moda: {moda}")


def calc_mediana(lista):
    lista = cond_lista(lista)
    print(f"Mediana: {stats.median(lista)}")


if __name__ == "__main__":
    print(cond_lista(lista))
    calc_media(lista)
    calc_mediana(lista)
    calc_moda(lista)
