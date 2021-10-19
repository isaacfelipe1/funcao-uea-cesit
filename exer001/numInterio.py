#crie uma função que receba um número inteiro como argumento, essa função deve repetir do 1 até o número informado pelo usuário, a quantidade do número em questão. ex: 1223334444
numero=int(input("Digite um número\n"))
def num(numero):
    t=1
    resul=0
    for t in range(1, numero):
        for t in range(t, numero):
            L=[]
            L=[t]
            print(L)

num(numero)