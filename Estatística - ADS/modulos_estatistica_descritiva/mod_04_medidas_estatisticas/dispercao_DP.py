"""
    Mediadas de Dispersão

    Dispersão - É o afastamento de todos os valores de uma série em relação a média aritmética ou mediana.
    De acordo com a grandeza dos afastamentos as séries estatísticas podem ser:
        Homogêneas (fraca dispersão quando Cv < 30%);
        Heterogêneas (forte dispersão quando Cv >= 30%);
        onde Cv é o coeficiente de variação.

        xi: 5, 5, 5, 5, 5 ⇒ dispersão nula
        yi: 4, 5, 6, 7 ⇒ fraca dispersão
        zi: 1, 2, 5, 8, 9 ⇒ forte dispersão
"""
import statistics as stats
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
    return desvio_padrao


def classifica_dp(lista):
    valor_dp = desvio_padrao(lista)
    lista = cond_lista(lista)
    media = stats.mean(lista)
    coef_variacao = (valor_dp / media) * 100
    print(f"Coeficiente de variação = {coef_variacao:.2f}%")
    if coef_variacao < 30:
        print("O grupo de dados da amostra é homogêneo devido coeficiente de variação ser menor que 30%.")
    else:
        print("O grupo de dados da amostra é heterogêneo devido coeficiente de variação ser maior ou igual a 30%.")



if __name__ == "__main__":
    lista = " 240 240 240 240 255 255 255 280 240 240 240 240 280 290 390 300 255 255 255 280 300 300 300 300"
    # lista = "2, 2, 2, 3, 4, 5, 6, 7, 8, 9"
    # lista = "5, 5, 5, 5, 5, 6"
    desvio = desvio_padrao(lista)
    print(f"Desvio padrão: {desvio:.2f}")
    classifica_dp(lista)
