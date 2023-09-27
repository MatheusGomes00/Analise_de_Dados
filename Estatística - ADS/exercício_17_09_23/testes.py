# import calculos as calc


# lista = " 2100 2500 4200 5000 5000 6400 10000 8400 17500 26500 26500 26500 26500"

# lista_tratada = calc.cond_lista(lista)
# qtde_linhas = calc.qtde_linhas(lista_tratada)

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

def cond_lista(lista):
    return list(sorted(map(int, lista.split())))


def percentil(lista, n_percent):
    lista = cond_lista(lista)
    position = int(len(lista) * n_percent) - 1
    print(lista[position])

lista = " 240 240 240 240 255 255 255 280 240 240 240 240 280 290 390 300 255 255 255 280 300 300 300 300"
quintil(lista, 4)
percentil(lista, 30)
