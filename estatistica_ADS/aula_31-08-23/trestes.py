# lista = [1, 2, 3, 4, 5]
# print(lista[-1])
# print(len(lista))
# print(int(len(lista) * 0.75))
# n = 1.75
# print(n, int(n), round(n))
def teste():
    def teste2(lista):
        lista_tratada = list(map(int, lista.split()))
        return sorted(lista)


numeros = "120	250	250	251	251	785	458	124	245	125 \
201	365	654	568	251	365	145	896	145	256 \
896	785	456	256	123	154	452	258	145	695 \
145	254	654	563	562	456	125	145	258	145 \
145	895	145	785	458	800	900	400	500	365 \
254	365	154	215	458	254	258	145	369	547 \
589	698	698	789	544	456	356	548	569	598"


# lista_tratada = list(sorted(map(int, lista.split())))
# print(lista_tratada)

# print(len(list(sorted(map(int, numeros.split())))))
#
# def quintil(lista, n_quintil):
#     lista = cond_lista(lista)
#     position = int(len(lista) * n_quintil) - 1
#
numeros = list(sorted(map(int, numeros.split())))

# print(int(len(numeros) * 7) - 1))
#

lista = "150	210	309	270	180	246	285	195	210	248 \
199	250	290	195	301	221	210	190	210	259"
lista = list(sorted(map(int, lista.split())))
print(lista)
position = int(len(lista) * (7 * 0.1) - 1)
print(f"Decil: {lista[position]}")
print(lista[9])
