# Calculadora em Python
# operações soma, subtração, multiplicação, divisão, potencia, raiz
# 
import math
import sys
sys.stdout.reconfigure(encoding='utf-8')

soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y
potencia = lambda x, y: x ** y
raiz = lambda x, y: x ** (1/y)

def menu():
    print("\n******************* Calculadora em Python *******************")
    print("\nSelecione o número da operação desejada: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potencia\n6 - Raiz\n")
    opcao = int(input("Digite sua opção (1/2/3/4/5/6): \n"))
    return opcao


while(True):
    opcao = menu()
    if opcao == 1:
        n1 = int(input("Entre com o primeiro valor: "))
        n2 = int(input("Entre com o segundo valor: "))
        print(f"\nA soma entre {n1} e {n2} é {soma(n1, n2)}")
    elif opcao == 2: 
        n1 = int(input("Entre com o primeiro valor: "))
        n2 = int(input("Entre com o segundo valor: "))
        print(f"\nA subtração entre {n1} e {n2} é {subtracao(n1, n2)}")
    elif opcao == 3: 
        n1 = int(input("Entre com o primeiro valor: "))
        n2 = int(input("Entre com o segundo valor: "))
        print(f"\nA multiplicação entre {n1} e {n2} é {multiplicacao(n1, n2)}")
    elif opcao == 4: 
        n1 = int(input("Entre com o primeiro valor: "))
        n2 = int(input("Entre com o segundo valor: "))
        print(f"\nA divisão entre {n1} e {n2} é {divisao(n1, n2):.2f}")
    elif opcao == 5: 
        n1 = int(input("Entre com o valor da base: "))
        n2 = int(input("Entre com o valor do expoente: "))
        print(f"\n{n1} elevado a  {n2} é igual a {potencia(n1, n2)}")
    elif opcao == 6: 
        n1 = int(input("Entre com o valor do radicando: "))
        n2 = int(input("Entre com o índice da raiz: "))
        print(f"\nA raiz {n2} de {n1} é {raiz(n1, n2):.2f}")
    else:
        print("\nerro")
    saida = input("\nContinue?\nS-sim N-não\t")
    if saida == 's':
        continue
    else:
        break
