import math
import statistics as stats
'''
Probabilidade Binomial
Prob(k) = (n, k) * P^k * Q^n-k
P = % busca
Q = resto
k = evento
n = tamanho da amosta
(n, k) = análise combinatória de n e k; n!/(n!*(n-k))
'''

lista = "5 1 14 22 8 16 14 4 19 6 10 15 10 4 11 14 18 10 9 11 8 8"


def cond_lista(lista):
    return sorted(list(map(int, lista.split())))


def calc_media(lista):
    lista = cond_lista(lista)
    media = stats.mean(lista)
    print(f"Média aritmética: {media:.2f}")


média = calc_media(lista)
n = 22
k = 10  # numero de vezes que o time fez gols acima da média
P = 0.45
Q = 0.55

an_comb = math.comb(n, k)

probabi = an_comb * (P**k) * (Q ** (n-k))

print(f"Resultado: {(probabi * 100):.2f}")
