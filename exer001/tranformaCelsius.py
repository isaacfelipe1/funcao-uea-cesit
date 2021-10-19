#5- crie uma função que receba uma valor de temperatura em Fahrenheit e transforme em clesius.
temperatura=int(input("Informe a temperatura em fahrenheit\n"))
def transformar(temperatura):
    grausCelsius=(temperatura-32)/1.8
    print(grausCelsius)

transformar(temperatura)