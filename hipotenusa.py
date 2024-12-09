import math 
def hipotenusa(cateto1:float,cateto2:float)-> float:
    """Função que recebe as medidas de dois catetos de um trianulo retangulo e devolve a medida da hipotenusa"""
    h= math.sqrt(cateto1 ** 2 + cateto2 **2)
    return h 

assert hipotenusa(3,4) == 5, "Função devia devolver 5"
print("Função passou todos os testes")