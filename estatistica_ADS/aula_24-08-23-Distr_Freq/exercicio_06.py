import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

#lista = "32 40 22 11 34 40 16 26 23 31 27 10 38 17 13 45 25 10 18 23 35 22 30 14 18 20 13 24 35 29 33 48 20 12 31 39 17 58 19 16 12 21 15 12 20 51 12 19 15 41 29 25 13 23 32 14 27 43 37 21 28 37 26 44 11 53 38 46 17 36 28 49 56 19 11"

lista = "25	26	29	20	22	24	25	25	25	26	26	27	28	28	28	28	29	29	20	20	23	24	25	26	27	27	28	29	29	30	31	36	36	36	38	38	41	42	45	57	58	52	56	58	45	25	26	28	29	36"


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
        print("De ", int(cont), " até", int(cont + intervalo), " = ", n_ocorrencia, '\t ', int(round((n_ocorrencia/len(lista)) * 100)), "%" )
        cont += intervalo


at = amplitude(lista_tratada)
k = qtde_linhas(len(lista_tratada))
intervalo = intervalo(at, k)
cont00 = min(lista_tratada)
print(f'n_linhas = ou {k[0]} ou {k[1]} ou {k[2]}')
print(f'Intervalo = de {int(intervalo)} em {int(intervalo)}\n')
cont_ocorrencias(lista_tratada, intervalo, cont00) 


# if __name__ == "__main__":
#     amplitude()
#     qtde_linhas()
#     intervalo()
#     cont_ocorrencias()
# # construir gráfico histograma de frequência
