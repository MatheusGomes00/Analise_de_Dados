"""
    * Os dados precisam estar ordenados. 
    * Mediana equivale ao Decil 5, Quartil 2 e Percentil 50.
    > Decil (Decil): Os decis dividem um conjunto de dados ordenados em dez partes iguais, 
    onde cada parte contém 10% das observações.
    > Quartil (Quartil): Os quartis dividem um conjunto de dados ordenados em quatro partes iguais, 
    onde cada parte contém 25% das observações. O primeiro quartil (Q1) é a mediana dos valores 
    abaixo da mediana geral, o segundo quartil (Q2) é a mediana geral e o terceiro quartil (Q3) é a mediana 
    dos valores acima da mediana geral.
    > Quintil (Quintil): Os quintis dividem um conjunto de dados ordenados em cinco partes iguais, 
    onde cada parte contém 20% das observações.
    > Percentil (Percentil): Os percentis são medidas que dividem um conjunto de dados ordenados 
    em 100 partes iguais, onde cada parte contém 1% das observações. O percentil 50 é a mediana, 
    e outros percentis (por exemplo, o percentil 25, o percentil 75) fornecem informações sobre 
    a distribuição dos dados.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')


lista = "25	26	29	20	22	24	25	25	25	26	26	27	28	28	28	28	29	29	20	20	23	24	25	26	27	27	28	29	29	30	31	36	36	36	38	38	41	42	45	57	58	52	56	58	45	25	26	28	29	36"

def cond_lista(lista):
    return sorted(list(map(int, lista.split())))


def decil(lista, n_decil):
    lista = cond_lista(lista)
    position = (int(len(lista) * (n_decil * 0.1)) - 1)
    print(f"Decil {n_decil} = {lista[position]}")


def quartil(lista, n_quartil):
    lista = cond_lista(lista)
    if n_quartil == 1:
        position = int(len(lista) * 0.25)
        print(f"Quartil {n_quartil}: {lista[position]}")
    elif n_quartil == 2:
        position = int(len(lista) * 0.5)
        print(f"Quartil {n_quartil}: {lista[position]}")
    elif n_quartil == 3:
        position = int(len(lista) * 0.75)
        print(f"Quartil {n_quartil}: {lista[position]}")
    elif n_quartil == 4:
        print(f"Quartil {n_quartil}: {lista[-1]}")
    else:
        print("Valor quartil inválido!")
    return


def quintil(lista, n_quintil):
    lista = cond_lista(lista)
    if n_quintil == 1:
        position = int(len(lista) * 0.2)
        print(f"Quintil {n_quintil}: {lista[position]}")
    elif n_quintil == 2:
        position = int(len(lista) * 0.4)
        print(f"Quintil {n_quintil}: {lista[position]}")
    elif n_quintil == 3:
        position = int(len(lista) * 0.6)
        print(f"Quintil {n_quintil}: {lista[position]}")
    elif n_quintil == 4:
        position = int(len(lista) * 0.8)
        print(f"Quintil {n_quintil}: {lista[position]}")
    elif n_quintil == 5:
        print(f"Quartil {n_quintil}: {lista[-1]}")
    else:
        print("Valor quartil inválido!")
    return


def percentil(lista, n_percent):
    lista = cond_lista(lista)
    position = int(len(lista) * (n_percent/100))
    print(f"Percentil {n_percent} = {lista[position - 1]}")


print(cond_lista(lista))
decil(lista, 7)
quartil(lista, 3)
quintil(lista, 4)
percentil(lista, 23)

