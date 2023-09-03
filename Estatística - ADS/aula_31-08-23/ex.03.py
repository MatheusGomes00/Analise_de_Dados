import statistics
# import numpy as np
# import sys
# import os
import exercicio_06 as ex

# sys.stdout.reconfigure(encoding='utf-8')


def verif_quartil(lista, n_quartil):
    if n_quartil == 1:
        position = int(len(lista) * 0.25)
        return lista[position]
    elif n_quartil == 2:
        position = int(len(lista) * 0.5)
        return lista[position]
    elif n_quartil == 3:
        position = int(len(lista) * 0.75)
        return lista[position]
    elif n_quartil == 4:
        return lista[-1]
    else:
        print("Valor quartil inválido!")
    return


def percentil(lista, n_percent):
    position = int(len(lista) * n_percent) - 1
    return lista[position]


numeros = "120	250	250	251	251	785	458	124	245	125 \
145	254	654	563	562	456	125	145	258	145 \
145	895	145	785	458	800	900	400	500	365 \
201	365	654	568	251	365	145	896	145	256 \
254	365	154	215	458	254	258	145	369	547 \
589	698	698	789	544	456	356	548	569	598 \
896	785	456	256	123	154	452	258	145	695 \
"
lista_tratada = list(map(int, numeros.split()))
media = statistics.mean(lista_tratada)
print(f"Média aritmética: {media:.2f}")

moda = statistics.mode(lista_tratada)
print(f"Moda: {moda}")

lista_ordenada = sorted(lista_tratada)
# print(lista_ordenada)
mediana = statistics.median(lista_ordenada)
print(f"Mediana: {int(mediana)}\t\tPosição 35 de 70: {lista_ordenada[35]} "
      f"\t\tPosição 36 de 70: {lista_ordenada[36]}")

print(f"Quartil 0{3}: {verif_quartil(lista_ordenada, n_quartil=3)}")

print(f"Percentil ..P{23}: {percentil(lista_ordenada, n_percent=0.23)}")

at = ex.amplitude(lista_ordenada)
k = ex.qtde_linhas(len(lista_ordenada))
intervalo = ex.intervalo(at, k)
cont00 = min(lista_ordenada)
print("\nFrequência")
print(f'n_linhas = ou {k[0]} ou {k[1]} ou {k[2]}')
print(f'Intervalo = de {int(intervalo)} em {int(intervalo)}\n')
ex.cont_ocorrencias(lista_tratada, intervalo, cont00)
