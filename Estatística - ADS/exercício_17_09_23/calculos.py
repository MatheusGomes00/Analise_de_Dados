import math
import statistics as stats
import numpy as np
import scipy.stats as stats2
import sys


# sys.stdout.reconfigure(encoding='utf-8')


def cond_lista(lista):
    return sorted(list(map(int, lista.split())))


def calc_moda(lista):
    lista = cond_lista(lista)
    moda = stats.mode(lista)
    print(f"Moda: {moda}")


def calc_media(lista):
    lista = cond_lista(lista)
    media = stats.mean(lista)
    print(f"Média aritmética: {media:.2f}")


def calc_mediana(lista):
    lista = cond_lista(lista)
    print(f"Mediana: {stats.median(lista)}")


def amplitude(lista):  # At
    xmax = max([x for x in lista])
    xmin = min([x for x in lista])
    return xmax - xmin


def qtde_linhas(lista):  # k
    opt0 = int(math.sqrt(len(lista)))
    opt1 = opt0 + 1
    opt2 = opt0 - 1
    return [opt2, opt0, opt1]  # ex.: opt0 = 7 então 6, 7, 8


def intervalo(amplitude, qtde_linhas):
    n_real = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(n_real)):
        for j in range(len(qtde_linhas)):
            if (amplitude + n_real[i]) % qtde_linhas[j] == 0:
                ic = (amplitude + n_real[i]) / qtde_linhas[j]
                return ic
            else:
                continue
    return "erro"


def hit_count(lista, intervalo, cont):
    while cont < max(lista):
        n_ocorrencia = 0
        for i in range(len(lista)):
            if lista[i] >= cont and lista[i] < cont + intervalo:
                n_ocorrencia += 1
        print("De ", int(cont), " até", int(cont + intervalo), " = ", n_ocorrencia,
              '\t ', int(round((n_ocorrencia/len(lista)) * 100)), "%")
        cont += intervalo


def verif_quartil(lista, n_quartil):
    #lista = cond_lista(lista)
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


def decil(lista, n_decil):
    lista = cond_lista(lista)
    position = (int(len(lista) * (n_decil * 0.1)) - 1)
    print(f"Decil: {lista[position]}")


def percentil(lista, n_percent):
    # lista = cond_lista(lista)
    position = int(len(lista) * n_percent) - 1
    return lista[position]


def calc_frequency(lista):
    lista_tratada = cond_lista(lista)
    at = amplitude(lista_tratada)
    k = qtde_linhas(len(lista_tratada))
    interval = intervalo(at, k)
    cont00 = min(lista_tratada)
    print(f'Frequência:\nn_linhas = ou {k[0]} ou {k[1]} ou {k[2]}')
    print(f'Intervalo = de {int(interval)} em {int(interval)}')
    hit_count(lista_tratada, interval, cont00)


def desvio_padrao(lista): # Desvio padrão de uma amostra  stats.stdev(lista_tratada) --> desvio padrão amostral dos dados
    lista_tratada = cond_lista(lista)
    media = sum(lista_tratada) / len(lista_tratada)
    soma_quadrados = 0
    for valor in lista_tratada:
        diferenca = valor - media  # desvios
        soma_quadrados += diferenca ** 2
    desvio_padrao = math.sqrt(soma_quadrados / (len(lista_tratada) -1))
    print(f"Desvio padrão: {desvio_padrao:.2f}")


def assimetria(lista):
    lista_tratada = cond_lista(lista)
    n = len(lista_tratada)
    media = stats.mean(lista_tratada)
    soma_cubos = 0
    for valor in lista_tratada:
        soma_cubos += ((valor - media) / stats.stdev(lista_tratada)) ** 3
    
    correcao = soma_cubos * (n / ((n-1) * (n-2)))
    print(f"Assimetria: {correcao:.2f}")


def coeficiente_per_curt(lista):  # coeficiente percentílico de curtose
    lista_tratada = cond_lista(lista)
    
    posit_q_1 = int(len(lista_tratada) * 0.25)
    posit_q_3 = int(len(lista_tratada) * 0.75)
    quartil_1 = lista_tratada[posit_q_1]
    quartil_3 = lista_tratada[posit_q_3]
    percentil_90 = percentil(lista_tratada, 90)
    percentil_10 = percentil(lista_tratada, 10)    
    curtose = (quartil_3 - quartil_1) / (2 * (percentil_90 - percentil_10))
    print(f"Curtose: {curtose}")

def curtose(lista):
    lista_tratada = cond_lista(lista)
    curtose = stats2.kurtosis(lista_tratada)
    print(f"Curtose: {curtose:.2f}")




lista = " 240 240 240 240 255 255 255 280 240 240 240 240 280 290 390 300 255 255 255 280 300 300 300 300"

lista = cond_lista(lista)
print(percentil(lista, 30))
verif_quartil(lista, 4)


# if __name__ == "__main__": ///oq que essa bagaça faz mesmo??
