import calculos as calc
import sys
import statistics as stats
sys.stdout.reconfigure(encoding='utf-8')


# lista = "2100	2500	2100	2500	2500	1600	2500	2100	3500	5300	5300	5300	5300"
lista = "240 240 240 240 255 255 255 280 240 240 240 240 280 290 390 300 255 255 255 280 300 300 300 300"

lista_tratada = calc.cond_lista(lista)
# print(type(calc.cond_lista(lista)))
calc.calc_media(lista)
calc.calc_mediana(lista)
calc.calc_moda(lista)
calc.desvio_padrao(lista_tratada)
lista_tratada = calc.cond_lista(lista_tratada) 
# print(stats.stdev(lista_tratada))
calc.assimetria(lista_tratada)
calc.curtose(lista_tratada)

