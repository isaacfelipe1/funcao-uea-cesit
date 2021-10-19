#8- Escreva um programa que contenha uma função que calcule o fatorial de um número inteiro.
n=int(input("Informe um valor\n"))

def fat(n):
    result=1
    for i in range(2, n+1):
        result*=i
        print(result)
fat(n)