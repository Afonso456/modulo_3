"""
Função que recebe três valores e devolve o maior caso sejam todos positivos e casosejam negativos deve devolver o menor,
 nos restantes casos devolve none
"""
def MaiorouMenor(a,b,c):
    if a > b:
        maior = a
    else:
        maior = b
    if maior < c:
        maior = c
    if a < b:
        menor = a
    else: 
        menor= b
    if c < menor:
        menor = c
    if a > 0 and b > 0 and c > 0:
        return maior
    if a < 0 and b < 0 and c < 0:
        return menor
    return None