#10 escreva um programa que contenha duas funções: um que guarde seu nome, telefone, site e e-mail numa variável do tipo lista, outro para exibir os dados dentro de um “Cartão”. Siga o modelo de saída abaixo.
nome=input("Informe o seu nome\n")
telefone=input("Informe seu número de telefone\n")
site= input("Informe seu site\n")
email=input("Informe seu email\n")
l=[]
def lista(nome, telefone,site,email):
    l=[nome, telefone,site,email]
lista(nome, telefone,site,email)

def mostrarTela(nome,telefone,site,email):
    print(nome)
    print("telefone:",telefone)
    print("Site:",site)
    print("Email:", email)
mostrarTela(nome,telefone,site,email)
