# from estatistica_ADS.modulos_estatistica_descritiva import mod_03_indicadores_estatisticos
# lista = "240 240 240 240 255 255 255 280 240 240 240 240 280 290 390 300 255 255 255 280 300 300 300 300"
# mod_03_indicadores_estatisticos.decil(lista, 5)
import statistics as stats
numeros = [i for i in range(500, 801)]

desvio = stats.stdev(numeros)
print(f"{numeros}\n{desvio:.2f}\n")



