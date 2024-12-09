"""
Função que recebe uma string e devolve true se todas as letras são iguais e false nos restantes casos
"""
def letras_iguais(texto):
    for letra in texto:
        if letra != texto[0]:
            return False    
        return True