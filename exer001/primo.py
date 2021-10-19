#9- Escreva um programa que contenha uma função que receba um número inteiro como parâmetro e retorne se ele é primo ou não.

numero=int(input("Informe um número\n"))

def primo(numero):
    total=0
    for c in range(1, numero+1):
        if numero%c==0:
            total+=1
    if total==2:
        print("é primo")
    else:
        print("Não é primo")

primo(numero)
