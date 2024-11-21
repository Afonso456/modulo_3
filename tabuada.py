#função que recebe um numero e calcula a sua tabuada
def tabuada(n):
    """
    Função que calcula e mostra a tabuada do numero que recebe
    Parametros
        n: nº inteiro
    Output 
        Tabuada  de 1 a 10 do n 
    """
    for i in range(1,11):
        x= n * i
        print(x)
tabuada(5)
