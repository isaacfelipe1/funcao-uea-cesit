#7- Escreva um programa que contenha uma função que receba dois números inteiros como paramentos: o primeiro será a base e o segundo, o expoente. A função retornará o valor do cálculo da potenciação destes números (base ^ expoente). Ex: base =2, expoente =3; a função retornará 8.
base=int(input("Informe a base\n"))
expoente=int(input("Informe o expoente\n"))


def potenciacao(base, expoente):
    print(base**expoente)

potenciacao(base, expoente)