#4- Faça uma função que calcule a área de um círculo. Insira o raio como argumento. Obs: faça a importação do math e use o r de lá.
import math
raio=float(input("Informe o raio\n"))

def circulo(raio):
    area=math.pi*math.pow(raio,2)
    print(area)

circulo(raio)