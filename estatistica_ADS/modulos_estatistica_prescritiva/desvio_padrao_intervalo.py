import statistics as stats
numeros = [i for i in range(500, 801)]

desvio = stats.stdev(numeros)
print(f"{numeros}\n{desvio:.2f}\n")



