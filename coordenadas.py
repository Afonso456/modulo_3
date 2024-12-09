#x= float(input("Insira a coordenada x:"))
#y= float(input("Insira a coordenada y:"))

def coordenadas(x,y):
    """
    Função que recebe do utilizador um numero e mostra/devolve a sua localização nos quandrantes
    """
    if x == 0 or y == 0:
        return "Sobre os eixos"
    if x > 0 and y > 0:
        return "1º quadrante"
    if x < 0 and y> 0:
        return"2º quadrante"
    if x < 0 and y < 0:
        return "3º quadrante"
    if x > 0 and y < 0:
        return "4º quadrante"

#print(coordenadas(x,y))

assert coordenadas(5,5) == "1º quadrante" , "A função não deu 1º quadrante"
assert coordenadas(-5,10) == "2º quadrante" , "A função não deu 2º quadrante"
assert coordenadas(-1,-1) == "3º quadrante" , "A função não deu 3º quadrante"
assert coordenadas(1,-3) == "4º quadrante" , "A função não deu 4º quadrante"
assert coordenadas(0,1) == "Sobre os eixos" , "Sobre os eixos"
print("A função passou todos os testes")