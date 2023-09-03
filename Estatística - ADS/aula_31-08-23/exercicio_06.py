import math
# import sys

# sys.stdout.reconfigure(encoding='utf-8')

numeros = "120	250	250	251	251	785	458	124	245	125 \
145	254	654	563	562	456	125	145	258	145 \
145	895	145	785	458	800	900	400	500	365 \
201	365	654	568	251	365	145	896	145	256 \
254	365	154	215	458	254	258	145	369	547 \
589	698	698	789	544	456	356	548	569	598 \
896	785	456	256	123	154	452	258	145	695"
lista_tratada = list(map(int, numeros.split()))
lista_ordenada = sorted(lista_tratada)

lista = "32 40 22 11 34 40 16 26 23 31 27 10 38 17 13 45 25 10 18 23 35 22 30 14 18 20 13 24 35 29 33 48 20 12 31 39 17 58 19 16 12 21 15 12 20 51 12 19 15 41 29 25 13 23 32 14 27 43 37 21 28 37 26 44 11 53 38 46 17 36 28 49 56 19 11"

lista_tratada = list(map(int, lista.split()))
# print(len(lista_tratada))
# print(lista)
# for i in range(len(lista_tratada)):
#     print(lista_tratada[i])


def amplitude(lista):  # At
    xmax = max([x for x in lista])
    xmin = min([x for x in lista])
    return xmax - xmin


def qtde_linhas(n_elementos):  # k
    opt0 = int(math.sqrt(n_elementos)) 
    opt1 = opt0 + 1
    opt2 = opt0 -1
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


def cont_ocorrencias(lista, intervalo, cont):
    while cont < max(lista):    
        n_ocorrencia = 0
        for i in range(len(lista)):
            if lista[i] >= cont and lista[i] < cont + intervalo:
                n_ocorrencia += 1
        print("De ", int(cont), " até", int(cont + intervalo), " = ", n_ocorrencia, '\t\t', int(round((n_ocorrencia/len(lista)) * 100)), "%" )
        cont += intervalo


if __name__ == "__main__":
    at = amplitude(lista_ordenada)
    k = qtde_linhas(len(lista_ordenada))
    interv = intervalo(at, k)
    cont00 = min(lista_ordenada)
    print(f'n_linhas = ou {k[0]} ou {k[1]} ou {k[2]}')
    print(f'Intervalo = de {int(interv)} em {int(interv)}\n')
    cont_ocorrencias(lista_ordenada, interv, cont00)
# # construir gráfico histograma de frequência
