#6- Defina uma função que pode aceitar duas strings como entrada e imprimir a string com maior comprimento. Se as duas strings têm o memso comprimento, a função deve imprimir todas as duas strings.
letra1=input("Digite a strings\n")
letra2=input("Digite outra string\n")
def string(str1,str2):
    if len(str1)>len(str2):
        print(str1)
    elif len(str1)==len(str2):
        print(str1)
        print(str2)
string(letra1,letra2)
