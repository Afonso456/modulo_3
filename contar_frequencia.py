"""
Para cada letra do alfabeto portugues indique o numero de vezes que aparece o numero de vezes que aparece na frase.
Todos os caracters que não pertencem ao alfabeto não são contabilizados
"""
def contar_letra(letra,frase):
    """
    Função que conta quantas vezes a letra aparece na frase
    """
    contar= 0
    for l in frase:
        if letra == l:
            contar += 1
    return contar
    
def contar_frequencia(frase):
    """
    Função que mostra o numero de vezes que cada letra do alfabeto aparece na frase
    """
    #percorrer o alfabeto
    for i in range (97,123):
        contar= contar_letra(chr(i),frase)
        print(contar)
    #mostrar o que a função devolveu

frase= input("Introduza uma frase:")
contar_frequencia(frase)    